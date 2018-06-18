import Queue

# The Queue class implements a basic first-in, first-out container.
# Elements are added to one "end" of sequence using put(),
# and removed from the other end using get().

q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
