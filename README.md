# Real-Time Data Engineering Pipeline Using Apache Kafka
## Detailed Technical Analysis Report

### Executive Summary
This comprehensive report provides an in-depth analysis of a real-time data engineering pipeline implemented using Apache Kafka. The project showcases an efficient approach to collecting, processing, and visualizing system performance metrics in real-time. By leveraging modern technologies such as Apache Kafka, Python, PostgreSQL, and Power BI, the pipeline creates a robust foundation for system monitoring and performance analysis. 

### 1. Technical Architecture

#### 1.1 Core Components
The pipeline architecture consists of four primary components:

1. **Data Collection Layer**: Responsible for gathering system metrics using Python's psutil library.
2. **Message Streaming Layer**: Implements Apache Kafka for real-time data streaming and message distribution.
3. **Storage Layer**: Employs PostgreSQL for persistent data storage and management.
4. **Visualization Layer**: Utilizes Microsoft Power BI for real-time dashboard creation and visual analytics.

#### 1.2 Technology Stack
The project leverages the following technologies:

- **Python Ecosystem**:
  - psutil: System and process utilities for metrics collection
  - kafka-python: Kafka client library for producer/consumer implementation
  - pyodbc: Database connectivity for PostgreSQL integration
- **Apache Stack**:
  - Kafka: Distributed streaming platform for real-time data processing
  - Zookeeper: Coordination service for managing the Kafka cluster
- **Database**: PostgreSQL for persistent data storage
- **Visualization**: Microsoft Power BI for real-time dashboard creation and data analysis


# How to Run
1. **Setting up Kafka:** Install Docker to use kafka.
```bash
docker stop kafka
docker stop zookeeper
docker rm kafka
docker rm zookeeper
```
2. **Database Setup:** Create a database and necessary table in 
POSTGESQL using the script provided in `table.sql`.

3. **Start the Apache Zookeeper and kafka server :**

```bash 
docker-compose up -d
```

4. **Create  kafka  topic :**

```bash 
docker exec -it kafka kafka-topics --create --topic iot_sensor_data --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
```
5. **Running the Pipeline:**

    #### 7.1 Install the requirements :

    ```bash 
    pip install requirements.txt
    ```
    #### 7.2 Run `data_pipeline.py` 
    to collect metrics data and send messages to Kafka topics, consume messages from Kafka topics and load data into POSTGRESQL.

8. **Dashboard Visualization:** Open `dashboard.pbix` in Power BI and connect to the POSTGRESQL database to visualize real-time metrics.