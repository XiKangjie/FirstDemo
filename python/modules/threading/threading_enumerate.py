import random
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s')

def worker():
    """thread worker function"""
    t = threading.currentThread()
    pause = random.randint(1, 5)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')

for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    # Joining the current thread introduces a deadlock situation, it must be skipped 
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()

"""
(Thread-1  ) sleeping 2
(Thread-2  ) sleeping 5
(Thread-3  ) sleeping 4
(MainThread) joining Thread-1
(Thread-1  ) ending
(MainThread) joining Thread-3
(Thread-3  ) ending
(MainThread) joining Thread-2
(Thread-2  ) ending
"""
