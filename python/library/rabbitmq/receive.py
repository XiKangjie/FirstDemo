#!/usr/bin/env python

import pika

connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# we can run the queue_declare as many time as we like, and only one will be created
# we need not declare the queue again if we were sure that the queue already exists.
channel.queue_declare(queue='hello')

# Whenever we receive a message, this callback function is called
def callback(ch, method, properties, body):
    print '[x] Received %r' % body

channel.basic_consume(callback, queue='hello', no_ack=True)

print '[*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
