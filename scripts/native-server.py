"""Start the API with project-local Windows settings and no container runtime."""
from pathlib import Path
import argparse
import os
import sys

ROOT=Path(__file__).resolve().parents[1]
API=ROOT/'apps'/'api'
# Own the file descriptors: PowerShell's output relay ends with the launcher.
log_dir=ROOT/'native-data'/'logs'
log_dir.mkdir(parents=True,exist_ok=True)
for descriptor,name in ((1,'api.log'),(2,'api-error.log')):
    stream=open(log_dir/name,'ab',buffering=0)
    os.dup2(stream.fileno(),descriptor)
    stream.close()
sys.stdout.reconfigure(encoding='utf-8',line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8',line_buffering=True)
parser=argparse.ArgumentParser()
parser.add_argument('--port',type=int,default=8000)
args=parser.parse_args()

from dotenv import dotenv_values
config=ROOT/'native-data'/'settings.env'
if not config.is_file():
    raise SystemExit('Native settings are missing. Complete native setup first.')
for key,value in dotenv_values(config).items():
    if value is not None:
        os.environ[key]=value
os.environ['LOCAL_ENV_FILE']=str(config)
os.environ['PYTHONIOENCODING']='utf-8'
os.chdir(API)
sys.path.insert(0,str(API))
import uvicorn
uvicorn.run('main:app',host='127.0.0.1',port=args.port,log_level='info')
