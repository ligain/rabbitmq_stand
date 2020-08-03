from datetime import datetime
from random import choice
from time import sleep

import pika

from examples.pika.constants import RABBITMQ_HOST, ROUTING_EXCHANGE, SEVERITIES

conn_params = pika.ConnectionParameters(host=RABBITMQ_HOST)
with pika.BlockingConnection(parameters=conn_params) as conn:
    channel = conn.channel()

    channel.exchange_declare(
        exchange=ROUTING_EXCHANGE,
        exchange_type='direct'
    )

    for _ in range(20):
        serverity = choice(SEVERITIES)
        msg = f'[{serverity}] at {datetime.utcnow().isoformat()}'
        channel.basic_publish(
            exchange=ROUTING_EXCHANGE,
            routing_key=serverity,
            body=msg
        )
        print(f'Msg: {msg} was sent to exchange: {ROUTING_EXCHANGE}')
        sleep(1)
