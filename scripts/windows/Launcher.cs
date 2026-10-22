using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Web.Script.Serialization;

[assembly:System.Reflection.AssemblyTitle("OpenTutor 本地学习")]
[assembly:System.Reflection.AssemblyVersion("1.0.0.0")]

internal static class Program {
    [STAThread]
    static int Main(string[] args) {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        string root = AppDomain.CurrentDomain.BaseDirectory.TrimEnd(Path.DirectorySeparatorChar);
        if (args.Length > 1 && args[0] == "--self-test") {
            var nativeStatus=Native.Run(root,"Status",20000).GetAwaiter().GetResult();
            var decodedStatus=new JavaScriptSerializer().Deserialize<System.Collections.Generic.Dictionary<string,object>>(nativeStatus.Output);
            using (var form = new Launcher(root, false)) {
                form.StartPosition=FormStartPosition.Manual; form.Location=new Point(-32000,-32000);
                form.ShowForTest(); form.PerformLayout(); Application.DoEvents();
                using (var bitmap = new Bitmap(form.Width, form.Height)) {
                    form.DrawToBitmap(bitmap, new Rectangle(Point.Empty, bitmap.Size));
                    bitmap.Save(args[1] + ".png");
                }
                File.WriteAllText(args[1], new JavaScriptSerializer().Serialize(new {
                    ok = File.Exists(Path.Combine(root, "scripts", "native-control.ps1")),
                    statusReadable = decodedStatus.ContainsKey("API") && decodedStatus.ContainsKey("Web"),
                    buttons = form.Controls.OfType<FlowLayoutPanel>().SelectMany(p => p.Controls.OfType<Button>()).Select(b => b.Text).ToArray(),
                    root = root
                }), new UTF8Encoding(false));
                form.CloseForTest();
            }
            return 0;
        }
        if (args.Length == 1 && (args[0] == "--start" || args[0] == "--stop" || args[0] == "--backup")) {
            var result = Native.Run(root, args[0].Substring(2), 180000).GetAwaiter().GetResult();
            return result.Code;
        }
        bool created;
        string identity = Convert.ToBase64String(Encoding.UTF8.GetBytes(root.ToLowerInvariant())).Replace('\\','_').Replace('/','_');
        using (var mutex = new Mutex(true, "Local\\OpenTutor_" + identity, out created)) {
            if (!created) {
                var result = Native.Run(root,"Start",180000).GetAwaiter().GetResult();
                if(result.Code == 0) { try { Process.Start("http://localhost:3001"); } catch { } }
                else MessageBox.Show("学习服务暂未就绪，请在已有启动器中查看状态或运行日志。","OpenTutor");
                return 0;
            }
            Application.Run(new Launcher(root, !args.Contains("--no-autostart")));
        }
        return 0;
    }
}

internal sealed class NativeResult {
    public int Code; public string Output;
}
internal static class Native {
    public static async Task<NativeResult> Run(string root, string action, int timeout) {
        string script = Path.Combine(root, "scripts", "native-control.ps1");
        if (!File.Exists(script)) return new NativeResult { Code=1, Output="找不到启动文件。请把启动器保留在 OpenTutor 项目文件夹内。" };
        string logDir=Path.Combine(root,"native-data","logs");
        Directory.CreateDirectory(logDir);
        string resultFile=Path.Combine(logDir,"launcher-"+DateTime.UtcNow.ToString("yyyyMMdd-HHmmss-fff")+"-"+action.ToLowerInvariant()+"-"+Guid.NewGuid().ToString("N")+".log");
        string command = "$ErrorActionPreference='Stop'; try { & '" + script.Replace("'", "''") + "' -Action '" + action + "' -NoBrowser *>&1 | Out-File -LiteralPath '" + resultFile.Replace("'", "''") + "' -Encoding utf8; exit $LASTEXITCODE } catch { $_ | Out-File -Append -LiteralPath '" + resultFile.Replace("'", "''") + "' -Encoding utf8; exit 1 }";
        var info = new ProcessStartInfo {
            FileName=Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System), "WindowsPowerShell", "v1.0", "powershell.exe"),
            Arguments="-NoProfile -ExecutionPolicy Bypass -EncodedCommand " + Convert.ToBase64String(Encoding.Unicode.GetBytes(command)),
            WorkingDirectory=root, UseShellExecute=false, CreateNoWindow=true, WindowStyle=ProcessWindowStyle.Hidden,

        };
        using (var process = Process.Start(info)) {
            bool completed = await Task.Run(() => process.WaitForExit(timeout)).ConfigureAwait(false);
            if (!completed) {
                try { process.Kill(); } catch { }
                string timeoutMessage="等待超时，请查看本地日志后重试。已有学习数据会保留。";
                try { File.AppendAllText(resultFile,Environment.NewLine+timeoutMessage,new UTF8Encoding(false)); } catch { }
                return new NativeResult {Code=1, Output=timeoutMessage};
            }
            string output=File.Exists(resultFile) ? File.ReadAllText(resultFile,Encoding.UTF8) : "";
            if(process.ExitCode!=0) {
                try { File.AppendAllText(Path.Combine(logDir,"launcher-error.log"),Environment.NewLine+"["+DateTime.UtcNow.ToString("o")+"] "+action+Environment.NewLine+output,new UTF8Encoding(false)); } catch { /* The individual operation file is still retained. */ }
            }
            if(process.ExitCode==0 && string.Equals(action,"Status",StringComparison.OrdinalIgnoreCase)) {
                try { File.Delete(resultFile); } catch { }
            }
            return new NativeResult {Code=process.ExitCode, Output=output};
        }
    }
}

internal sealed class Launcher : Form {
    readonly string root;
    readonly bool autoStart;
    readonly Label status = new Label();
    readonly TextBox detail = new TextBox();
    readonly FlowLayoutPanel actions = new FlowLayoutPanel();
    readonly NotifyIcon tray = new NotifyIcon();
    readonly System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
    bool busy, quitting, testing;
    static readonly Color Ink=Color.FromArgb(27,43,43), Muted=Color.FromArgb(89,104,104);
    public Launcher(string location, bool start) {
        root=location; autoStart=start;
        Text="OpenTutor · 本地学习"; ClientSize=new Size(560,350); MinimumSize=new Size(570,380);
        StartPosition=FormStartPosition.CenterScreen; Font=new Font("Microsoft YaHei UI",10); BackColor=Color.FromArgb(245,248,246);
        Icon=Icon.ExtractAssociatedIcon(Application.ExecutablePath);
        var title = new Label {Text="OpenTutor 本地学习", Font=new Font(Font.FontFamily,21,FontStyle.Bold), ForeColor=Ink, Location=new Point(26,22), AutoSize=true};
        var subtitle = new Label {Text="课程与学习进度保存在这台电脑上", ForeColor=Muted, Location=new Point(28,70), AutoSize=true};
        status.Text="准备就绪"; status.ForeColor=Ink; status.Location=new Point(28,107); status.Size=new Size(500,24);
        actions.Location=new Point(24,144); actions.Size=new Size(520,88); actions.WrapContents=true;
        AddButton("启动并打开学习", async () => await Operate("Start",true));
        AddButton("打开学习页面", () => { Open("http://localhost:3001"); return Task.FromResult(0); });
        AddButton("停止学习服务", async () => await Operate("Stop",false));
        AddButton("备份学习数据", async () => await Operate("Backup",false));
        AddButton("打开备份文件夹", () => { Folder("local-backups"); return Task.FromResult(0); });
        AddButton("查看运行日志", () => { Folder(Path.Combine("native-data","logs")); return Task.FromResult(0); });
        detail.Location=new Point(28,242); detail.Size=new Size(502,48); detail.Multiline=true; detail.ReadOnly=true; detail.BorderStyle=BorderStyle.None;
        detail.BackColor=BackColor; detail.ForeColor=Muted; detail.Text="双击此程序即可开始学习，无需打开 Docker。";
        var footer=new Label {Text="关闭此窗口会收起到托盘；停止服务后可释放运行内存。", ForeColor=Muted, Font=new Font(Font.FontFamily,9), Location=new Point(28,312), AutoSize=true};
        Controls.AddRange(new Control[] {title,subtitle,status,actions,detail,footer});
        var menu=new ContextMenuStrip();
        menu.Items.Add("打开启动器", null, (s,e) => {Show(); WindowState=FormWindowState.Normal; Activate();});
        menu.Items.Add("打开学习页面", null, (s,e) => Open("http://localhost:3001"));
        menu.Items.Add("停止学习服务", null, async (s,e) => {if(!busy) await Operate("Stop",false);});
        menu.Items.Add("备份学习数据", null, async (s,e) => {if(!busy) await Operate("Backup",false);});
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add("退出启动器（服务继续运行）", null, (s,e) => {quitting=true; Close();});
        tray.Icon=Icon; tray.Text="OpenTutor 本地学习"; tray.ContextMenuStrip=menu;
        tray.DoubleClick += (s,e) => {Show(); WindowState=FormWindowState.Normal; Activate();};
        timer.Interval=30000; timer.Tick += async (s,e) => { if (!busy) await RefreshStatus(); };
        Shown += async (s,e) => {if(testing)return; tray.Visible=true; timer.Start(); if(autoStart) await Operate("Start",true); else await RefreshStatus();};
        FormClosing += (s,e) => {if(!quitting && e.CloseReason==CloseReason.UserClosing){e.Cancel=true;Hide();}};
        FormClosed += (s,e) => {timer.Stop(); timer.Dispose(); tray.Dispose();};
    }
    public void ShowForTest() {testing=true; Show();}
    public void CloseForTest() {quitting=true; Close();}
    void AddButton(string text, Func<Task> action) {
        var button=new Button {Text=text, AutoSize=true, MinimumSize=new Size(156,34), FlatStyle=FlatStyle.Flat, BackColor=Color.White, ForeColor=Ink, Margin=new Padding(4)};
        button.FlatAppearance.BorderColor=Color.FromArgb(209,220,213);
        button.Click += async (s,e) => {try {await action();} catch {status.Text="操作未完成";detail.Text="请查看本地运行日志，学习记录会保留。";}};
        actions.Controls.Add(button);
    }
    async Task Operate(string action, bool browser) {
        if(busy)return;
        busy=true; actions.Enabled=false;
        status.Text=action=="Start"?"正在准备学习环境…":action=="Stop"?"正在停止服务…":"正在备份本地数据…";
        try {
            var result=await Native.Run(root,action,180000);
            if(result.Code!=0) {status.Text="操作未完成";detail.Text="请点击“查看运行日志”了解原因。学习记录会保留。"; return;}
            status.Text=action=="Start"?"学习服务已就绪":action=="Stop"?"已停止，可释放运行内存":"备份已完成";
            detail.Text=action=="Start"?"浏览器关闭后服务仍可继续运行；用完可点击“停止学习服务”。":action=="Stop"?"课程、资料和学习进度均已保留。下次双击启动器即可继续。":"完整备份包含学习数据库、上传资料和模型设置，可在备份文件夹查看。";
            if(browser)Open("http://localhost:3001");
        } catch {status.Text="操作未完成";detail.Text="请检查项目文件是否完整，并查看本地运行日志。";}
        finally {busy=false;actions.Enabled=true;}
    }
    async Task RefreshStatus() {
        busy=true;
        try {
            var result=await Native.Run(root,"Status",20000);
            var data=new JavaScriptSerializer().Deserialize<System.Collections.Generic.Dictionary<string,object>>(result.Output);
            status.Text=(bool)data["API"] && (bool)data["Web"] ? "学习服务正在运行" : "学习服务已停止或尚未完整启动";
        } catch {status.Text="状态暂不可用，可尝试启动";} finally {busy=false;}
    }
    void Folder(string path) {var full=Path.Combine(root,path);Directory.CreateDirectory(full);Open(full);}
    static void Open(string path) {try {Process.Start(path);} catch {MessageBox.Show("无法打开，请确认系统默认浏览器和文件关联正常。","OpenTutor");}}
}
