from kafka import KafkaProducer
from celery import shared_task

@shared_task
def send():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    err = producer.send('test', b'Hello, World!')
    producer.flush()
    print(err.__dict__)

from kafka import KafkaConsumer
@shared_task
def receive():
    consumer = KafkaConsumer('test',  bootstrap_servers='kafka:9092')
    # print(consumer)
    for message in consumer:
        print ("---------------------------------->", message)