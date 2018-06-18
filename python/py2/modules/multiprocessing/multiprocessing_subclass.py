import multiprocessing
import time
import random
import logging
import thread
import objgraph

count = 0
queue = multiprocessing.Queue(1)
queue.put(0)

log = logging.getLogger(__name__)

class Worker(multiprocessing.Process):

    queue = queue

    def run(self):
        #log.warn("run")
        print thread.get_ident()
        count = queue.get()
        print 'In %s, count: %s' % (self.name, count)
        self.queue.put(count+1)
        time.sleep(random.randint(2, 3))
        count = queue.get()
        self.queue.put(count-1)
        print 'In %s, count: %s' % (self.name, count-1)
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        count = queue.get()
        print '@@', i, count
        queue.put(count)
        p.start()
    for j in jobs:
        j.join()
    objgraph.show_most_common_types(limit=20)
