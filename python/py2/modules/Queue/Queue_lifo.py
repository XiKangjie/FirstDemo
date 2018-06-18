import Queue

# In contrast to the standard FIFO implementation of Queue, the LifoQueue uses last-in,
# first-out ordering (normally associated with a stack data structure).
q = Queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
