import multiprocessing
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

pool = None

def f(x):
    logger.info('processing x: %s' % x) 
    t = random.randint(1, 10)
    time.sleep(t)
    return x * x, t

def print_result(result):
    print result

def main():
    global pool
    # maxtasksperchild is the number of tasks a worker process can complete before
    # it will exit and be replaced with a fresh worker process, to enable unused
    # resources to be freed. The default maxtasksperchild is None, 
    # which means worker processes will live as long as the pool.
    pool = multiprocessing.Pool(processes=4, maxtasksperchild=2)

    results = []
    for i in range(1, 100):
        result = pool.apply_async(f, args=(i,), callback=print_result)
        results.append(result)

    # some processes may have finished before result.get()
    for result in results:
        try:
            r, t = result.get(timeout=2)
            print 'r: %s, t: %s' % (r, t)
        except multiprocessing.TimeoutError:
            print 'timeout'

if __name__ == '__main__':
    main()
