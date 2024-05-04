import shlex
import subprocess

command = 'ls -l '

process = subprocess.Popen(
    shlex.split(command),
    stdout=subprocess.PIPE,
    stderr = subprocess.STDOUT, 
)
    
for line in iter(process.stdout.readline, ""):
    pass