from kafka import KafkaProducer
import json
import time
import random

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to generate fake transaction data
def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(10, 5000), 2),
        "timestamp": time.time(),
        "location": random.choice(["New York", "San Francisco", "London", "Mumbai", "Tokyo"]),
        "device": random.choice(["Mobile", "Laptop", "Tablet"]),
        "status": random.choice(["Approved", "Declined"])
    }

# Send multiple transactions to Kafka
for _ in range(10):  # Sending 10 transactions
    transaction = generate_transaction()
    producer.send('transactions', transaction)
    print(f"Sent: {transaction}")
    time.sleep(1)  # Simulating real-time data stream

# Close producer
producer.flush()
producer.close()
