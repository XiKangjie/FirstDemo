import threading
import time

def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)    # use default name

t.start()
w.start()
w2.start()

"""
my_service Starting
worker Starting
Thread-1 Starting
my_service Exiting
worker Exiting
Thread-1 Exiting
"""
