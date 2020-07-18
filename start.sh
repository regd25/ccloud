export COMPOSE_FILE=local.yml
docker-compose up -d
docker rm -f django
docker-compose run --rm --service-ports django
