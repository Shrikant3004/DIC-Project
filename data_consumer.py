import psycopg2
from psycopg2.extras import RealDictCursor
from confluent_kafka import Consumer, KafkaException, KafkaError
from datetime import datetime
import json
from config import PSQL_HOST,PSQL_DATABASE,PSQL_PASSWORD,PSQL_USER

def consume():
    # Kafka Consumer configuration
    conf = {
        'bootstrap.servers': 'localhost:9092',  # Update with your Kafka broker
        'group.id': 'iot-consumer-group',
        'auto.offset.reset': 'earliest',  # To read messages from the beginning
    }

    consumer = Consumer(conf)
    
    # Subscribe to the 'iot_sensor_data' topic
    consumer.subscribe(['iot_sensor_data'])

    try:
        # PostgreSQL setup
        pg_conn = psycopg2.connect(host=PSQL_HOST, database=PSQL_DATABASE, user=PSQL_USER, password=PSQL_PASSWORD, cursor_factory=RealDictCursor,port='5432')
        pg_cursor = pg_conn.cursor()

        while True:
            # Poll for new messages
            msg = consumer.poll(1.0)  # Timeout of 1 second

            if msg is None:
                # No message received within the timeout period
                continue
            if msg.error():
                # Handle error
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition, no action needed
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                else:
                    raise KafkaException(msg.error())

            # Process the message
            message_value = msg.value().decode('utf-8')  # Assuming your data is sent as UTF-8 encoded string
            values = message_value.split(',')
            # Unpack the values into variables
            current_datetime, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage = values

            # Insert data into PostgreSQL
            pg_cursor.execute("INSERT INTO Performance (time,cpu_usage,memory_usage,cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (datetime.now(),cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free,
                bytes_sent, bytes_received, disk_usage))
            pg_conn.commit()

            # print(f"Inserted data into PostgreSQL: {values}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Close connections
        consumer.close()
        pg_cursor.close()
        pg_conn.close()
        print("Consumer and database connections closed.")

