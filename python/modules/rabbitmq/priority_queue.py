#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# RabbitMQ has priority queue implementation in the core as of version 3.5.0.

# You can declare priority queues using the x-max-priority argument. 
# This argument should be an integer indicating the maximum priority the queue should support. 
args = {'x-max-priority': 10}
channel.queue_declare(queue='priority_queue', durable=True, arguments=args)

if len(sys.argv) != 3:
    print 'Usage: %s message priority' % sys.argv[0]
    sys.exit(1)
message = sys.argv[1]
priority = int(sys.argv[2])

# publish prioritised messages using the priority field of basic.properties.
# Larger numbers indicate higher priority.
channel.basic_publish(exchange='',
                      routing_key='priority_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                          priority=priority
                          )
                      )
print '[x] Sent %r' % message

connection.close()
