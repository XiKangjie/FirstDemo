import subprocess

# parames have sapces, use '\' to escape.
cmd = ['sudo', 'sed', '-i', 's/net.ipv4.ip_forward\ =\ 0/net.ipv4.ip_forward\ =\ 1/g', '/etc/sysctl.conf']
subprocess.call(cmd)
