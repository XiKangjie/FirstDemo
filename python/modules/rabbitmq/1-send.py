#!/usr/bin/env python
import pika

# The first thing we need to do is to establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Next, before sending we need to make sure the recipient queue exists
queue_info = channel.queue_declare(queue='hello')
#queue_info = channel.queue_declare(queue='hello', durable=True)
print queue_info.method.message_count

# In RabbitMQ a message can never be sent directly to the queue, it always need
# an exchange, the default exchange is identified by an emtpy string.
# routing_key specifies queue name.
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print '[x] Sent "Hello World!"'

# Before exiting the program we need to make sure the network buffers were flushed
# and message was actually delivered to RabbitMQ.
connection.close()
