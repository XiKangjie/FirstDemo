import subprocess

proc = subprocess.Popen(['echo', 'to stdout'],
                        stdout=subprocess.PIPE)
stdout_val, _ = proc.communicate()
print 'stdout:', repr(stdout_val)

# stdout: 'to stdout\n'
