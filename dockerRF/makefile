build:
	@docker build -t dockerrfpy27 --network=host .

run:
	@docker-compose up -d

stop:
	@docker stop dockerrfpy27

down:
	@docker-compose down

runkafka:
	@docker run --rm -d -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 --net=host -e ADV_HOST=172.22.0.1 --name dkafka landoop/fast-data-dev

stopkafka:
	@docker stop dkafka

listen: 
	@cd py && python3 kafkaConsumeRunCommand.py &

jenkins:

	@cd py && python3 jenkinsCreateJobs.py &


