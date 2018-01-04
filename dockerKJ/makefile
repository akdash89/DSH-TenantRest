build:
	@docker build -t dockerkj --network=host .

run:
	@xhost + && docker run --rm -d -e DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v PATHTOMOUNTEDDISK:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 jenkinsCreateJobs.py

runnod:
	@xhost + && docker run --rm -e DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v PATHTOMOUNTEDDISK:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 jenkinsCreateJobs.py

stop:
	@docker stop dockerkj

runall: chown run listen

runonce:
	@sudo chmod 777 changeme.sh && ./changeme.sh

runkafka:
	@docker run --rm -d -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 --net=host -e ADV_HOST=IPADDRESS --name dkafka landoop/fast-data-dev

stopkafka:
	@docker stop dkafka

chown:
	@sudo chmod 777 /var/run/docker.sock

listennod:
	@docker run -ti --rm -e DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v PATHTOMOUNTEDDISK:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 kafkaConsumeRunCommand.py

listen:
	@docker run -ti --rm -d -e DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v PATHTOMOUNTEDDISK:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 kafkaConsumeRunCommand.py



