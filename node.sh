sudo apt-get update
curl -fsSL https://get.docker.com | sh
cd .. 
git clone https://github.com/Gozargah/Marzban-node
cd Marzban-node && docker compose up -d
nano /var/lib/marzban-node/ssl_client_cert.pem
nano docker-compose.yml
docker compose down && docker compose up -d
