from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'transactions',  # Topic Name
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest'  # Start reading from the beginning of the topic
)

print("Consumer is listening for transactions...")

# Read transactions from Kafka topic
for message in consumer:
    transaction = message.value
    print(f"Received Transaction: {transaction}")
