# Alarms are a special sort of signal, where your program asks the OS to notify it
# after some period of time has elapsed.

import signal
import time

def received_alarm(signum, stack):
    print 'Alarm:', time.ctime()

# Call received_alarm in 2 seconds.
signal.signal(signal.SIGALRM, received_alarm)
signal.alarm(2)

print 'Before:', time.ctime()
time.sleep(4)
print 'After:', time.ctime()

# The call to sleep() does not last the full 4 seconds.

"""
Before: Sun Jan 18 13:57:25 2015
Alarm: Sun Jan 18 13:57:27 2015
After: Sun Jan 18 13:57:27 2015
"""
