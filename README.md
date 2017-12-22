Summary for usage:
1. Download/clone directory
2. Put all your tests into 'Testcases' folder
3. cd into projectfolder
4. sudo make (only to do once)
5. sudo make run


Additional info
run .robot files
- go cd into top project directory (e.g. DSH)
- run : source venv/bin/activate
- cd into folder where tests are located
- run : pybot test.robot

https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile
docker:

Note: robotframework-mqttlibrary has no python 3 support therefore we use python 2.7