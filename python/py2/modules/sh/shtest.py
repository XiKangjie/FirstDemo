# sh is fa full-fledged subprocess interface for Python that allows you to call
# any program as if it were a function.

from __future__ import print_function

import sh

# NOTE here ifconfig() is not Python function, it is running the binary commands
# on your system dynamically by resolving your $PATH, much like Bash does.
# In this way, all the programs on your system are easily available to you from
# within Python.
print(sh.ifconfig('eth0'))

# same thing as above
# from sh import ifconfig
# print(ifconfig('eth0'))


# arguments
print(sh.ls('-l', '/'))

# glob expansion
print(sh.ls(sh.glob('*.py')))

# sub-commands
print(sh.git.status())
print(sh.git('status'))

# exit codes
output = sh.ls()
print(output.exit_code)
