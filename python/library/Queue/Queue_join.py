import Queue

q = Queue.Queue()
q.put(1)
q.get()
q.task_done()

# If a join() is currently blocking, it will resume when all items
# have been processed (meaning that a task_done() call was received
# for every item that had been put() into the queue).

q.join()
