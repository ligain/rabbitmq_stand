# RabbitMQ tutorial
It's my walk through of tutorial [https://www.rabbitmq.com/getstarted.html](https://www.rabbitmq.com/getstarted.html)

# Pre-install  
0) First of all `docker` should be installed on your local machine.
```
$ docker --version
Docker version 18.09.7, build 2d0083d
```
1) Clone this repository
```bash  
$ git clone https://github.com/ligain/rabbitmq_stand
``` 
2) Go to project folder
```bash  
$ cd rabbitmq_stand/
```
3) Create python env
```
$ python3 -m venv venv
```
4) Activate python env
```
$ source ./venv/bin/activate
```
5) Install `pip` requirements
```
$ pip install -r requirements.txt
```
6) Launch project
```bash  
$ docker-compose up
```

### 1) Example of simple producer/consumer
[https://www.rabbitmq.com/tutorials/tutorial-one-python.html](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
Run consumer
```
$ python3 ./examples/pika/simple_consumer.py
```
Run producer
```
$ python3 ./examples/pika/simple_producer.py
```
### 2) Example of work queues
[https://www.rabbitmq.com/tutorials/tutorial-two-python.html](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
Run consumer. It's recommended to run multiple consumers.
```
$ python3 .examples/pika/work_queue_consumer.py
$ python3 .examples/pika/work_queue_consumer.py
```
Run producer
```
$ python3 .examples/pika/work_queue_producer.py
```

### 3) Example of pub-sub producer/consumer
[https://www.rabbitmq.com/tutorials/tutorial-three-python.html](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
Run consumer. It's recommended to run multiple consumers.
```
$ python3 .examples/pika/pubsub_consumer.py
$ python3 .examples/pika/pubsub_consumer.py
```
Run producer
```
$ python3 .examples/pika/pubsub_producer.py
```

### 4) Example of routing producer/consumer
[https://www.rabbitmq.com/tutorials/tutorial-four-python.html](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
Run consumer. It's recommended to run multiple consumers.
```
$ python3 .examples/pika/routing_consumer.py
$ python3 .examples/pika/routing_consumer.py
```
Run producer
```
$ python3 .examples/pika/routing_producer.py
```

### 5) Example of topic exchange
[https://www.rabbitmq.com/tutorials/tutorial-five-python.html](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)
Run consumer. It's recommended to run multiple consumers.
```
$ python3 .examples/pika/topic_consumer.py
$ python3 .examples/pika/topic_consumer.py
```
Run producer
```
$ python3 .examples/pika/topic_producer.py
```

# Project Goals 
The code is written for educational purposes.