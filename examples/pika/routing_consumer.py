import sys
import pika

from examples.pika.constants import RABBITMQ_HOST, ROUTING_EXCHANGE

severities = sys.argv[1:]


def process_msg(channel, method, properties, body):
    print(f'Received msg: "{body}"')


conn_params = pika.ConnectionParameters(host=RABBITMQ_HOST)
with pika.BlockingConnection(conn_params) as conn:
    chanel = conn.channel()

    random_queue = chanel.queue_declare(
        queue='',
        exclusive=True
    )
    random_queue_name = random_queue.method.queue

    chanel.exchange_declare(
        exchange=ROUTING_EXCHANGE,
        exchange_type='direct'
    )

    for severity in severities:
        chanel.queue_bind(
            exchange=ROUTING_EXCHANGE,
            routing_key=severity,
            queue=random_queue_name
        )

    chanel.basic_consume(
        queue=random_queue_name,
        on_message_callback=process_msg,
        auto_ack=True
    )
    print('Waiting for messages')
    chanel.start_consuming()



