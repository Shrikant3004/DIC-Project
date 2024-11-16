
docker stop kafka
docker stop zookeeper
docker rm kafka
docker rm zookeeper


docker-compose up -d
docker exec -it kafka kafka-topics --create --topic iot_sensor_data --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092