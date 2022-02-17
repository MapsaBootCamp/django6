#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='payam_mostaghim', exchange_type='direct')

result2 = channel.queue_declare(queue='', exclusive=True)
queue_name2 = result2.method.queue
print("queue name: ", queue_name2)

channel.queue_bind(exchange='payam_mostaghim', routing_key='salm_safe_ou', queue=queue_name2)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback2(ch, method, properties, body):
    print(" [x] safe salam safe ou%r" % json.loads(body))


channel.basic_consume(
    queue=queue_name2, on_message_callback=callback2, auto_ack=True)

channel.start_consuming()