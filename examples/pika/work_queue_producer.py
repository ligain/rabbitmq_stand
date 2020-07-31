from datetime import datetime
from time import sleep

import pika

from examples.pika.constants import WORK_QUEUE, RABBITMQ_HOST

params = pika.ConnectionParameters(host=RABBITMQ_HOST)
with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    # create or get persistent queue
    channel.queue_declare(WORK_QUEUE, durable=True)

    for _ in range(20):
        msg = f'Msg from producer {datetime.utcnow().isoformat()}'
        channel.basic_publish(
            exchange='',
            routing_key=WORK_QUEUE,
            body=msg,
            properties=pika.BasicProperties(delivery_mode=2)  # makes messages persistent
        )
        print(f'Sent "{msg}" to queue: {WORK_QUEUE}')
        sleep(2)
