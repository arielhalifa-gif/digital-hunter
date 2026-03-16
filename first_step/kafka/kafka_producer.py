import json
from confluent_kafka import Producer


class Producer:
    @staticmethod
    def send_to_topic(data, reason):
        producer_config = {
            "bootstrap.servers": "localhost:9092"
        }

        data['reason'] = reason
        producer = Producer(producer_config)
        value = json.dumps(data).encode("utf-8")

        producer.produce(
            topic="intel_signals_dlq",
            value=value,
        )

        producer.flush()
