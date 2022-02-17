#!/usr/bin/env python
import pika, sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='CL2', durable=True)
message = ' '.join(sys.argv[1:]) or "June madaret ziad goal nazan!"

channel.basic_publish(exchange='', routing_key='CL2', body=message, properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(f" [x] Sent {message}")
connection.close()