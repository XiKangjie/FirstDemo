import multiprocessing
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

pool = None

def f(x):
    logger.info('processing x: %s' % x) 
    time.sleep(random.randint(1, 10))
    return x * x

def print_result(result):
    print result

def main():
    global pool
    pool = multiprocessing.Pool(processes=4, maxtasksperchild=2)

    results = []
    for i in range(1, 10):
        result = pool.apply_async(f, args=(i,), callback=print_result)
        results.append(result)
    for result in results:
        try:
            result.get(timeout=3)
        except multiprocessing.TimeoutError:
            print 'timeout'

if __name__ == '__main__':
    main()
