Summary for usage:
1. DISPLAY=your_host_ip:0
2. xhost +
4. sudo docker build -t dockerkj --network=host .
4. docker run -ti --rm        -e DISPLAY=$DISPLAY  -v /home/rakeshlaptop/Documents/projects/DSH/mountedDisk:/py/mountedDisk       -v /tmp/.X11-unix:/tmp/.X11-unix        dockerkj python3 jenkinsCreateJobs.py
5. https://github.com/RakiP/Testcases.git
6. docker run -ti --rm -e DISPLAY=$DISPLAY -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v /home/rakeshlaptop/Documents/projects/DSH/mountedDisk:/py/mountedDisk -v /tmp/.X11-unix:/tmp/.X11-unix dockerkj python3 kafkaConsumeRuncommand.py

docker run -v /py/mountedDisk/Testcases:/robot/Testcases -v /py/mountedDisk/Testresults:/robot/Testresults -w /robot --net=host rpartapsing/dsh:part1 /bin/bash -c ./runscript.sh