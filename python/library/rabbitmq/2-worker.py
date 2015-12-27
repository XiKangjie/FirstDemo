#!/usr/bin/env python

import pika
import time

connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# Whenever we receive a message, this callback function is called
def callback(ch, method, properties, body):
    print '[x] Received %r' % body
    time.sleep(body.count('.'))
    print '[x] Done'
    # Message acknowledgment

    # send ack to tell RabbitMQ that a particular message had been received,
    # processed and that RabbitMQ is free to delete it.
    
    # If a consumer dies (its channel is closed, connection is closed, or 
    # TCP connection is lost) without sending an ack, RabbitMQ will understand
    # that a message wasn't processed fully and will re-queue it. 
    # If there are other consumers online at the same time, it will then quickly
    # redeliver it to another consumer. That way you can be sure that no message
    # is lost, even if the workers occasionally die.

    # There aren't any message timeouts, RabbitMQ will redeliver the message
    # only when the worker connection dies.
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Fair dispatch
# This tell RabbitMQ not to give more than one message to a worker at a time.
# In other words, don't dispatch a new message to a worker until it has
# processed and acknowledged the previous one.
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='task_queue')

channel.start_consuming()
