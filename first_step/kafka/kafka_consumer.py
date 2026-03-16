import json
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "targets",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)






class Consumer:
    @staticmethod
    def listen_intel():
        consumer.subscribe(["Intel"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("❌ Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")
                target = json.loads(value)
                yield target
        except KeyboardInterrupt:
            print("\n🔴 Stopping consumer")
        finally:
            consumer.close()



    @staticmethod
    def listen_attack():
        consumer.subscribe(["Attack"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("❌ Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")
                target = json.loads(value)
                yield target
        except KeyboardInterrupt:
            print("\n🔴 Stopping consumer")
        finally:
            consumer.close()



    @staticmethod
    def listen_damage():
        consumer.subscribe(["Damage"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("❌ Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")
                target = json.loads(value)
                yield target
        except KeyboardInterrupt:
            print("\n🔴 Stopping consumer")
        finally:
            consumer.close()
        