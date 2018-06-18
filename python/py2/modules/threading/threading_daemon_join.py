import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s')

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# To wait until a daemon thread has completed its work, use the join() method.
# By default, join() blocks indefinitely. It is also possible to pass a timeout
# argument (a float representing the number of seconds to wait for the thread
# to become inactive). If the thread does not complete within the timeout period,
# join() returns anyway.

d.join(1)
print 'd.isAlive', d.isAlive()
t.join()


"""
(daemon    ) Starting
(non-daemon) Starting
(non-daemon) Exiting
d.isAlive True
"""
