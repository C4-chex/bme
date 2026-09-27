f = open("D:\杂\讲话.txt",'r',编码方式)      open(文件路径，操作方式)   
                                   r：只读   w：写入
                                    编码方式一般有中文的话写  encoding='utf-8'
print(f.read(#字节数))             不写字节数默认全读
不过大型文件一般使用readline 即一行一行的读

不过
    因为要close
    所有一般使用的是with as的形式 使文件被读取之后自动关闭
    eg： with open (.....) as #变量名
            #要tab缩进 
            #操作 如print