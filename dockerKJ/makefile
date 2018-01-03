build:
	@docker build -t dockerkj --network=host .

run:
	@xhost + && docker run -d -e DISPLAY  -v /home/rakeshlaptop/Documents/projects/DSH/mountedDisk:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 jenkinsCreateJobs.py

runnod:
	@xhost + && docker run -e DISPLAY  -v /home/rakeshlaptop/Documents/projects/DSH/mountedDisk:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 jenkinsCreateJobs.py

stop:
	@docker stop dockerkj

runkafka:
	@docker run --rm -d -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 --net=host -e ADV_HOST=172.22.0.1 --name dkafka landoop/fast-data-dev

stopkafka:
	@docker stop dkafka

listen:
	@docker run -ti --rm -d -e DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v /home/rakeshlaptop/Documents/projects/DSH/mountedDisk:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 kafkaConsumeRunCommand.py



