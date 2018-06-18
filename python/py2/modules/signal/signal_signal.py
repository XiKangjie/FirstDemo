import signal
import os
import time

# The arguments to signal handler are the signal number and the stack frame from
# the point in you program that was interrupted by the signal.
def receive_signal(signum, stack):
    print 'Received:', signum

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print 'My PID is:', os.getpid()

while True:
    print 'Waiting...'
    time.sleep(3)
