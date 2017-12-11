import pwd
import grp
import os

def chown(path, user, recursive=True):
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(user).gr_gid
    os.chown(path, uid, gid)
    if recursive:
        for root, dirs, files in os.walk(path):
            for momo in dirs:
                os.chown(os.path.join(root, momo), uid, gid)
            for momo in files:
                os.chown(os.path.join(root, momo), uid, gid)
    else:
        os.chown(path, uid, gid)

chown('/etc/uwsgi/', 'consen')
