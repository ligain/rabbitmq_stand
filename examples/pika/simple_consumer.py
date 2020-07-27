import pika

from examples.pika.constants import SIMPLE_QUEUE

params = pika.ConnectionParameters(host='0.0.0.0', port=5672)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


with pika.BlockingConnection(params) as conn:
    channel = conn.channel()

    # create a queue with name 'simple'
    channel.queue_declare(SIMPLE_QUEUE)

    channel.basic_consume(
        queue=SIMPLE_QUEUE,
        auto_ack=True,
        on_message_callback=callback
    )

    print('Waiting for messages')
    channel.start_consuming()
