from datetime import datetime
from time import sleep

import pika

from examples.pika.constants import RABBITMQ_HOST, LOG_EXCHANGE

params = pika.ConnectionParameters(host=RABBITMQ_HOST)

with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    channel.exchange_declare(
        exchange=LOG_EXCHANGE,
        exchange_type='fanout'
    )
    for _ in range(20):
        msg = f'Log message: {datetime.utcnow().isoformat()}'
        channel.basic_publish(
            exchange=LOG_EXCHANGE,
            routing_key='',
            body=msg
        )
        print(f'Sending message: {msg}')
        sleep(1)

