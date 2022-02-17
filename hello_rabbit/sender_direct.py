#!/usr/bin/env python
import pika, sys
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='payam_mostaghim', exchange_type='direct')
queue_name = ' '.join(sys.argv[1:]) or "June madaret ziad goal nazan!"

channel.basic_publish(exchange='payam_mostaghim', routing_key=queue_name, body=json.dumps("salam"))
print(f" [x] Sent {message}")
connection.close()