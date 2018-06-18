import subprocess

cmd = 'ls ; ls'
subprocess.check_call(cmd, shell=True)
