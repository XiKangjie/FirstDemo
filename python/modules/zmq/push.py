import zmq
import struct

# define a string of size 4[MB] 
msgToSend = struct.pack('i', 45) * 1000

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://127.0.0.1:5000")
#socket.connect("ipc:///tmp/zmqpushpull")

# print the message size in bytes
print len(msgToSend)

socket.send(msgToSend)

print "Sent message"
