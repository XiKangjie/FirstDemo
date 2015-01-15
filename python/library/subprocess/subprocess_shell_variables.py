import subprocess

subprocess.call(['ls', '-l'], shell=True)


# setting the shell argument to a true value causes subprocess to spawn an
# intermediate shell process, and tell it to run the command.
# using an intermediate shell means that variables, glob patterns, and other
# special shell features in the command string are processed before the
# command is run.
subprocess.call('echo $HOME', shell=True)
