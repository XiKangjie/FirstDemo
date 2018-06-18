import psutil

for p in psutil.process_iter():
    cmdline = p.cmdline()
    if len(cmdline) > 1 and "qemu-system-i386" in cmdline[0] and "name %s" % "test" in " ".join(cmdline[1:]):
        print p.cmdline()
        print p.pid
        p.kill()
