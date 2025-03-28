sudo docker build -t backend_api:latest ./backend/
sudo docker stack rm op_project
sudo docker stack deploy -c docker-compose.yml op_project
