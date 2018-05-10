import pika


# Set the connection parameters to connect to rabbit-server1 on port 5672
# on the / virtual host using the username "guest" and password "guest"
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('127.0.0.1',
                                       5672,
                                       '/',
                                       credentials)
# credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='User1', exchange_type='fanout')
channel.exchange_declare(exchange='User2', exchange_type='fanout')

channel.queue_declare(queue='Device1', exclusive=True)
channel.queue_declare(queue='Device2', exclusive=True)
channel.queue_declare(queue='Device3', exclusive=True)

channel.queue_bind(exchange='User1', queue='Device1')
channel.queue_bind(exchange='User2', queue='Device2')
channel.queue_bind(exchange='User2', queue='Device3')
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback, queue='Device1', no_ack=True)
# channel.basic_consume(callback, queue='Device2', no_ack=True)
# channel.basic_consume(callback, queue='Device3', no_ack=True)
channel.start_consuming()
