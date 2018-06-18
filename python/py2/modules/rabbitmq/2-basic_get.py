import pika
import time

connection = pika.BlockingConnection()
channel = connection.channel()

def init_conn():
    global connection, channel
    connection = pika.BlockingConnection()
    channel = connection.channel()

while True:
    try:
        method_frame, header_frame, body = channel.basic_get('task_queue')
        if method_frame:
            print(method_frame, header_frame, body)
            if method_frame.redelivered:
                channel.basic_ack(method_frame.delivery_tag)
                print "redelivered"
                continue
            time.sleep(60)
            channel.basic_ack(method_frame.delivery_tag)
            print 'done'
        else:
            print('No message returned')
        time.sleep(10)
    except pika.exceptions.ConnectionClosed:
        print 'connection closed'
        init_conn()
        time.sleep(5)
