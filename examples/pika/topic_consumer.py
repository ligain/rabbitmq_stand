import sys
from random import choice

import pika

from examples.pika.constants import RABBITMQ_HOST, TOPIC_EXCHANGE, FACILITIES, SEVERITIES

conn_params = pika.ConnectionParameters(host=RABBITMQ_HOST)


def receive_callback(channel, method, properties, body):
    print(f'Received msg: {body}')


with pika.BlockingConnection(conn_params) as conn:
    channel = conn.channel()

    if sys.argv[1:]:
        binding_keys = sys.argv[1:]
    else:
        facility = choice(FACILITIES)
        severity = choice(SEVERITIES)
        binding_keys = f'{facility}.{severity}'

    channel.exchange_declare(
        exchange=TOPIC_EXCHANGE,
        exchange_type='topic'
    )
    channel.queue_declare(
        queue=binding_keys,
        exclusive=True
    )
    channel.queue_bind(
        queue=binding_keys,
        exchange=TOPIC_EXCHANGE,
        routing_key=binding_keys
    )

    channel.basic_consume(
        queue=binding_keys,
        on_message_callback=receive_callback,
        auto_ack=True
    )

    print(f'Waiting for messages from {binding_keys} queue...')
    channel.start_consuming()
