import pika
from datetime import datetime

from examples.pika.constants import SIMPLE_QUEUE, RABBITMQ_HOST

params = pika.ConnectionParameters(host=RABBITMQ_HOST)
with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    # create a queue with name 'simple'
    channel.queue_declare(SIMPLE_QUEUE)

    channel.basic_publish(
        exchange='',
        routing_key='simple',
        body=f'Msg to {SIMPLE_QUEUE} queue {datetime.utcnow().isoformat()}'
    )

