# $ fab git_pull -f env.py
# $ fab git_pull:repo=dotfiles -f env.py

from fabric.api import *
from fabric.contrib.console import confirm

# It is important to know that these command-line switches are interpreted before 
# your fabfile is loaded: any reassignment to env.hosts or env.roles in your
# fabfile will overwrite them.
# If you wish to nondestructively merge the command-line hosts with your fabfile-defined ones
# env.hosts.extend(['host1', host2])
env.hosts = ['10.16.66.180', 'xikangjie@10.16.66.181']
env.user = 'xikangjie'

def git_pull(repo='demo'):
    repo_dir = '/home/%s/github/%s' % (env.user, repo)
    print repo_dir
    with cd(repo_dir):
        # warn_only specifies to warn, instead of abort.
        with settings(warn_only=True):
            result = run('git pull')
        if result.failed and not confirm('git pull failed, continue anyway?'):
            abort('Aborting at user request.')

"""
$ fab git_pull:repo=dotfiles -f env.py -u xikangjie
[10.16.66.180] Executing task 'git_pull'
/home/xikangjie/github/dotfiles
[10.16.66.180] run: git pull
[10.16.66.180] Login password for 'xikangjie': 
[10.16.66.180] out: Updating c8d51c4..1e21725
[10.16.66.180] out: error: Your local changes to 'tmux/tmux.conf' would be overwritten by merge.  Aborting.
[10.16.66.180] out: Please, commit your changes or stash them before you can merge.
[10.16.66.180] out: 


Warning: run() received nonzero return code 1 while executing 'git pull'!

git pull failed, continue anyway? [Y/n] y
[10.16.66.181] Executing task 'git_pull'
/home/xikangjie/github/dotfiles
[10.16.66.181] run: git pull
[10.16.66.181] out: Already up-to-date.
[10.16.66.181] out: 


Done.
Disconnecting from 10.16.66.181... done.
Disconnecting from 10.16.66.180... done.
"""
