import json
from kafka import KafkaConsumer

KAFKA_TOPIC = "topic"
KAFKA_SERVER = "localhost:9092"
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_SERVER])

for msg in consumer:
    if msg is not None:
        kafka_data = json.loads(msg.value.decode('utf-8'))
        print(kafka_data)
