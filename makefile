bundle:
	npm install && npm run bundle
development: 
	docker-compose up
production: 
	docker-compose -f docker-compose.prod.yml up -d
down: 
	docker-compose down --remove-orphans
build:
	docker build . -t drf-boilerplate