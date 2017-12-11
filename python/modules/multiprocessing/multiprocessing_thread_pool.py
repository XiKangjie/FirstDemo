from multiprocessing.pool import ThreadPool, TimeoutError
import time
import logging
import random
import multiprocessing

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

pool = None

def f(x):
    logger.info('processing x: %s' % x) 
    t = random.randint(1, 10)
    #time.sleep(t)

    # if use process pool multiprocessing.Pool,
    # AssertionError: daemonic processes are not allowed to have children
    p = multiprocessing.Process(target=time.sleep, args=(t,))
    p.start()
    p.join()

    return x * x, t

def print_result(result):
    print result

def main():
    global pool
    pool = ThreadPool(processes=4)

    results = []
    for i in range(1, 10):
        result = pool.apply_async(f, args=(i,), callback=print_result)
        results.append(result)
    for result in results:
        result.get()

if __name__ == '__main__':
    main()
