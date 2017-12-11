#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

# Temporary queues
# Firstly, whenever we connect to Rabbit we need a fresh, empty queue.
# To do it we could create a queue with a random name
# Secondly, once we disconnect the consumer the queue should be deleted.
# There's an exclusive flag for that.
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# Bindings
channel.queue_bind(exchange='logs', queue=queue_name)

print '[x] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print '[x] %r' % body

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
