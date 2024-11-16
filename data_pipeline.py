from data_producer import produce_data
from data_consumer import consume
import psycopg2
import threading
import time
from config import PSQL_HOST,PSQL_DATABASE,PSQL_PASSWORD,PSQL_USER
from psycopg2.extras import RealDictCursor


def producer_thread(start_time):
    while True:
        try:
            produce_data()
            # Sleep for a short interval before consuming the next message
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in producer_thread: {str(e)}")

def consumer_thread(start_time):
    while True:
        try:
            consume()
            # Sleep for a short interval before consuming the next message
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in consumer_thread: {str(e)}")

def delete_thread(start_time):
    pg_conn = psycopg2.connect(host=PSQL_HOST, database=PSQL_DATABASE, user=PSQL_USER, password=PSQL_PASSWORD, cursor_factory=RealDictCursor,port='5432')
    pg_cursor = pg_conn.cursor()
    while True:
            # Sleep for 5 seconds
            time.sleep(5)

            # Delete all records from the 'Performance' table
            pg_cursor.execute("DELETE FROM Performance")
            pg_conn.commit()

start_time = time.time()
# Create separate threads for producer and consumer
producer_thread = threading.Thread(target=producer_thread, args=(start_time,))
consumer_thread = threading.Thread(target=consumer_thread, args=(start_time,))
delete_thread =  threading.Thread(target=delete_thread,args=(start_time,))

# Start the threads
producer_thread.start()
consumer_thread.start()
delete_thread.start()

# Wait for the threads to finish (which will never happen in this case as they run infinitely)
producer_thread.join()
consumer_thread.join()
delete_thread.join()