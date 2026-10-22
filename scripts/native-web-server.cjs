// The child inherits real log file handles, independent of the launcher process.
const fs = require('fs');
const path = require('path');
const {spawn} = require('child_process');
const root = path.resolve(__dirname, '..');
const logs = path.join(root, 'native-data', 'logs');
fs.mkdirSync(logs, {recursive:true});
const output = fs.openSync(path.join(logs, 'web.log'), 'a');
const errors = fs.openSync(path.join(logs, 'web-error.log'), 'a');
const server = spawn(process.execPath, [path.join(root, 'apps/web/node_modules/next/dist/bin/next'),
  'start', '--hostname', '127.0.0.1', '--port', '3001'], {
  cwd:path.join(root, 'apps/web'), windowsHide:true, stdio:['ignore', output, errors]
});
server.on('error', error => {fs.writeSync(errors, String(error)+'\n');process.exitCode=1;});
server.on('exit', code => {fs.closeSync(output);fs.closeSync(errors);process.exitCode=code??1;});
