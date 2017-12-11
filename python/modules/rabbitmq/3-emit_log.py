#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')
# The messages will be lost if no queue is bound to the exchange yet, but that's
# okay for us; if no consumer is listening yet we can safely discard the message.

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print '[x] Sent %r' % message
connection.close()
