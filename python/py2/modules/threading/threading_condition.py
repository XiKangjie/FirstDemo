import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s (%(threadName)-2s) %(message)s')

def consumer(cond):
    """Wait for the condition and use the ressource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """Set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resouce available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

"""
2015-01-07 10:10:32,916 (c1) Starting consumer thread
2015-01-07 10:10:34,921 (c2) Starting consumer thread
2015-01-07 10:10:36,924 (p ) Starting producer thread
2015-01-07 10:10:36,925 (p ) Making resouce available
2015-01-07 10:10:36,925 (c1) Resource is available to consumer
2015-01-07 10:10:36,926 (c2) Resource is available to consumer
"""
