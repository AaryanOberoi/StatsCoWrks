docker exec rabbit rabbitmqctl list_queues > devices.txt
docker exec rabbit rabbitmqctl list_exchanges > users.txt
python -m libs.upload