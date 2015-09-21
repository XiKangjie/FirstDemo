import pebble
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def f(x):
    logger.info('processing x: %s' % x) 
    t = random.randint(1, 10)
    time.sleep(t)
    return x * x, t

def task_done(task):
    try:
        print dir(task)
        print task.get()
    except pebble.TimeoutError:
        print 'timeout'

def main():
    
    # timeout is an integer, if greater than zero, once expired will force
    # the timed out task to be interrupted and the worker will be restarted;
    with pebble.process.Pool(workers=4, task_limit=4) as pool:
        for i in range(1, 100):
            pool.schedule(f, args=(i,), callback=task_done, timeout=2)

    # without task_done, without TimeoutError
    #with pebble.process.Pool(workers=4, task_limit=4) as pool:
        #for i in range(1, 100):
            #pool.schedule(f, args=(i,), timeout=2)

    # not work as expected, why ???
    #pool = pebble.process.Pool(workers=4, task_limit=4)
    #for i in range(1, 100):
        #pool.schedule(f, args=(i,), callback=task_done, timeout=2)

if __name__ == '__main__':
    main()
