import sys
from datetime import datetime
from time import sleep
from random import choice

import pika

from examples.pika.constants import RABBITMQ_HOST, TOPIC_EXCHANGE, FACILITIES, SEVERITIES

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

conn_params = pika.ConnectionParameters(host=RABBITMQ_HOST)

with pika.BlockingConnection(conn_params) as conn:
    channel = conn.channel()

    channel.exchange_declare(
        exchange=TOPIC_EXCHANGE,
        exchange_type='topic'
    )

    for _ in range(100):
        if sys.argv and len(sys.argv) > 2:
            routing_key = sys.argv[1]
        else:
            facility = choice(FACILITIES)
            severity = choice(SEVERITIES)
            routing_key = f'{facility}.{severity}'

        msg = f'[{routing_key}] Log message at {datetime.utcnow().isoformat()}'
        channel.basic_publish(
            exchange=TOPIC_EXCHANGE,
            routing_key=routing_key,
            body=msg
        )
        print(f'Sent log message: "{msg}" to {routing_key}')
        sleep(0.1)
