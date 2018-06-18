import subprocess

proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE)
proc.communicate('stdin: to stdin\n')

# stdin: to stdin
