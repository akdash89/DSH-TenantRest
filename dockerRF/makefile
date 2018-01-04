build:
	@docker build -t dockerrfpy27 --network=host .

run:
	@docker-compose up -d

runnod:
	@docker-compose up

stop:
	@docker stop dockerrfpy27

down:
	@docker-compose down

runonce:
	@sudo chmod 777 changeme.sh && ./changeme.sh

runkafka:
	@docker run --rm -d -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 --net=host -e ADV_HOST=IPADDRESS --name dkafka landoop/fast-data-dev

stopkafka:
	@docker stop dkafka


