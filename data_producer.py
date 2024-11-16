import requests
from confluent_kafka import Producer
import json
import random
import time
from datetime import datetime
import psutil

def get_pc_specs():
    current_datetime = datetime.now()
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_interrupts = psutil.cpu_stats().interrupts
    cpu_calls = psutil.cpu_stats().syscalls
    memory_used = psutil.virtual_memory().used
    memory_free = psutil.virtual_memory().free
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_received = psutil.net_io_counters().bytes_recv
    disk_usage = psutil.disk_usage('/').percent
    # Produce data to Kafka topic
    message = f"{current_datetime}, {cpu_usage}, {memory_usage}, {cpu_interrupts},{cpu_calls},{memory_used},{memory_free},{bytes_sent},{bytes_received},{disk_usage}"
    return message


# Kafka producer configuration using Confluent Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Update with your Kafka broker
}

producer = Producer(conf)
topic = 'iot_sensor_data'

def produce_data():
    try:
        data = get_pc_specs()
        if data:
            producer.produce(topic, value=data, callback=delivery_report)
            # print(f"Produced: {data}")
            producer.flush()  # Ensure all messages are delivered
    except Exception as error:
        print(f"Error: {error}")

# Delivery report callback to confirm message delivery
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    # else:
        # print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
