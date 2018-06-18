# the Queue module has been renamed to queue in Python 3
import queue
import threading
from urllib.request import urlopen
import time

hosts = ["http://www.yahoo.com", "http://www.google.com", "http://www.amazon.com",
		"http://www.ibm.com", "http://www.apple.com"]

que = queue.Queue()

class ThreadUrl(threading.Thread):
	def __init__(self, que):
		threading.Thread.__init__(self)
		self.que = que

	def run(self):
		while True:
			# grabs host from queue
			host = self.que.get()
			# grabs urls of hosts and prints first 1024 bytes of page
			response = urlopen(host)
			print(response.read(1024))
			# signals to queue job is done
			self.que.task_done()


start = time.time()
def main():
	# spawn a pool of threads, and pass them queue instance
	for i in range(5):
		t = ThreadUrl(que)
		t.setDaemon(True)
		t.start()

	# populate queue with data
	for host in hosts:
		que.put(host)

	# wait on the queue until everything has been processed
	que.join()

main()
print("Elapsed Time: {0}".format(time.time() - start))