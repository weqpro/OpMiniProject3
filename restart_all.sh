#docker build -t backend_api:latest ./backend
#docker build -t frontend_app:latest ./frontend/frontend-fortis

sudo docker build -t backend_api:latest ./backend/
sudo docker build -t frontend_app:latest ./frontend/frontend-fortis/
sudo docker stack rm op_project
sudo docker stack deploy -c docker-compose.yml op_project
