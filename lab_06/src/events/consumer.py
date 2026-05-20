import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq")
)

channel = connection.channel()

channel.exchange_declare(
    exchange="hotel_events",
    exchange_type="topic"
)

channel.queue_declare(queue="hotel_events_queue")

channel.queue_bind(
    exchange="hotel_events",
    queue="hotel_events_queue",
    routing_key="#"
)

def callback(ch, method, properties, body):

    print("Событие было получено.....................................")
    print(body.decode())


channel.basic_consume(
    queue="hotel_events_queue",
    on_message_callback=callback,
    auto_ack=True
)

print("..........................=)............................")

channel.start_consuming()