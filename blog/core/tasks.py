from post.kafka_producer import receive


@shared_task
def start_receive():
    print("RUNNNNNNNNNNNNNNNNNN")

start_receive.delay