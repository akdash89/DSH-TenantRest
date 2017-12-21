Summary for usage:
1. Download/clone directory
2. Put all your tests into 'Testcases' folder
3. cd into projectfolder
4. sudo make (only to do once)
5. sudo make start


run .robot files
- go cd into top project directory (e.g. DSH)
- run : source venv/bin/activate
- cd into folder where tests are located
- run : pybot test.robot

https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile
docker:
- make dockerfile
- login to docker, run: sudo docker login
- cd into the folder of the Dockerfile
- run: sudo docker build -t dockerrfpy27 .
- run: sudo docker tag dockerrfpy27 rpartapsing/dsh:part1
- check if rpartapsing/dsh is there, run: docker image ls
- run: sudo docker push rpartapsing/dsh:part1
- run: sudo docker run \
           -e ROBOT_TESTS=Testcases \
           dshrf
- run: sudo docker-compose up
or run: sudo docker-compose up --exit-code-from robot-framework-target

check logs:
- run: sudo docker ps 
- copy id
- run: sudo docker logs {copied id}

get into container:
- run: sudo docker ps 
- copy id
- run: sudo docker exec -it {copied id} bash 

Link Kafka container en RobotFramework container
- start kafka first and make it run on the background:
sudo docker run -d -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 -e ADV_HOST=127.0.0.1 --name dkafka landoop/fast-data-dev
- then start robot framework container:
sudo docker run --rm -it --name drf --link dkafka:kafka rpartapsing/dsh:part1 bash


Note: robotframework-mqttlibrary has no python 3 support we need to downgrade


