#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.queue_purge(queue='task_queue')
channel.queue_purge(queue='lightvm_one_files')

connection.close()
