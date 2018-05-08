docker exec rabbit rabbitmqctl list_queues > devices.txt
docker exec rabbit rabbitmqctl list_exchanges > users.txt
python -n libs.upload