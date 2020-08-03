import pika

from examples.pika.constants import RABBITMQ_HOST, LOG_EXCHANGE

params = pika.ConnectionParameters(host=RABBITMQ_HOST)


def receive_callback(channel, method, properties, body):
    print(f'Received log: {body}')


with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    channel.exchange_declare(
        exchange=LOG_EXCHANGE,
        exchange_type='fanout'
    )

    random_queue = channel.queue_declare(queue='', exclusive=True)
    random_queue_name = random_queue.method.queue
    channel.queue_bind(
        exchange=LOG_EXCHANGE,
        queue=random_queue_name
    )

    channel.basic_consume(
        queue=random_queue_name,
        on_message_callback=receive_callback,
        auto_ack=True
    )

    print('Waiting for messages.')
    channel.start_consuming()

