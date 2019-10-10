bundle:
	npm install && npm run bundle
up: 
	docker-compose up
detach: 
	docker-compose -f docker-compose.prod.yml up -d
down: 
	docker-compose down --remove-orphans
build:
	docker build . -t drf-boilerplate