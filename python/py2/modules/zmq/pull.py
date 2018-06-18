import zmq
import struct

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5000")
#socket.bind("ipc:///tmp/zmqpushpull")

count = 0
while True:
    count += 1
    # receive the message
    msg = socket.recv()

    print "[{0}]Message Size is: {1} [MB]".format( count, len(msg) / (1000 * 1000) )
