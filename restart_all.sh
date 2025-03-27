sudo docker build backend_api:latest
sudo docker stack rm op_project
sudo docker stack deploy -c docker-compose.yml op_project
