#!/usr/bin/env python

import pika
import time

connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

args = {'x-max-priority': 10}
channel.queue_declare(queue='priority_queue', durable=True, arguments=args)

# Whenever we receive a message, this callback function is called
def callback(ch, method, properties, body):
    print '[x] Received %r, priority: %s' % (body, properties.priority)
    time.sleep(body.count('.'))
    print '[x] Done'
    # Message acknowledgment
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Fair dispatch
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='priority_queue')

channel.start_consuming()
