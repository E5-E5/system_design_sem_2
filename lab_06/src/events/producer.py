import json
import pika
import time


class EventProducer:

    # def __init__(self):

    #     connected = False

    #     while not connected:

    #         try:

    #             self.connection = pika.BlockingConnection(
    #                 pika.ConnectionParameters(host="rabbitmq")
    #             )

    #             connected = True

    #         except Exception:

    #             print("RabbitMQ not ready, retrying...")
    #             time.sleep(5)

    #     self.channel = self.connection.channel()

    #     self.channel.exchange_declare(
    #         exchange="hotel_events",
    #         exchange_type="topic"
    #     )

    def publish(self, routing_key: str, message: dict):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")
        )

        channel = connection.channel()

        channel.exchange_declare(
            exchange="hotel_events",
            exchange_type="topic"
        )

        channel.basic_publish(
            exchange="hotel_events",
            routing_key=routing_key,
            body=json.dumps(message)
        )

        connection.close()