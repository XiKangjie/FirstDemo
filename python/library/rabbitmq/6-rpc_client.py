#!/usr/bin/env python
import pika
import uuid
import sys

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        # A client sends a request message and a server replies with a response message. 
        # In order to receive a response the client needs to send a 'callback' queue address with the request. 
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

n = sys.argv[1]
if not n:
    print >> sys.stderr, 'Usage: %s [number]...' % sys.argv[0]
    sys.exit(1)
print(" [x] Requesting fib(n)")
response = fibonacci_rpc.call(n)
print(" [.] Got %r" % response)
