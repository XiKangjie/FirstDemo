#!/usr/bin/env python

import pika

connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# we can run the queue_declare as many time as we like, and only one will be created
# we need not declare the queue again if we were sure that the queue already exists.
# we are not yet sure which program to run first, it's a goog practice to repeat declaring
# the queue in both programs.
channel.queue_declare(queue='hello')

# Whenever we receive a message, this callback function is called
def callback(ch, method, properties, body):
    print '[x] Received %r' % body

channel.basic_consume(callback, queue='hello', no_ack=True)

print '[*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
