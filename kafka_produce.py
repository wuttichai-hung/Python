import json
from pykafka import KafkaClient

KAFKA_TOPIC = 'topic'
KAFKA_SERVER = 'localhost:9092'
client = KafkaClient(hosts=KAFKA_SERVER)

topic = client.topics[KAFKA_TOPIC]
producer = topic.get_sync_producer()

producer_msg = {"a":30}
message_encode = json.dumps(producer_msg).encode('utf-8')
producer.produce(message_encode)
print("Sent: ", message_encode)
