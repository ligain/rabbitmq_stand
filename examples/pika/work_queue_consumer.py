import time

import pika

from examples.pika.constants import WORK_QUEUE, RABBITMQ_HOST

params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672)


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(1)
    print(f" [x] Msg was processed {body} {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    # create or get persistent queue
    channel.queue_declare(WORK_QUEUE, durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=WORK_QUEUE,
        on_message_callback=callback
    )

    print('Waiting for messages')
    channel.start_consuming()
