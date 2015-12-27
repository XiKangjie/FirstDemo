#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Two things are required to make sure that messages aren't lost:
# we need to mark both the queue and messages as durable.

# Message durability
# we need to mark both the queue and messages are durable to make sure
# that messages aren't lost even if RabbitMQ restart.
channel.queue_declare(queue='task_queue', durable=True)

# Round-robin dispatching

message = ' '.join(sys.argv[1:]) or 'Hello World!'
# we need to mark our messages as persistent - by supplying a delivery_mode
# property with a value 2.
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2) # make message persistent
                      )
print '[x] Sent %r' % message

connection.close()
