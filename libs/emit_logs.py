import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='User1',
                         exchange_type='fanout')
#channel.exchange_declare(exchange='User2',
#                         exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='User1',
                      routing_key='Device1',
                      body=message)
channel.basic_publish(exchange='User2',routing_key='Device2',body=message)
print(" [x] Sent %r" % message)
connection.close()