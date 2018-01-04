import os
from os.path import expanduser

home = expanduser("~")

absFilePath = os.path.dirname(os.path.abspath(__file__))
dMountedDiskClient = os.path.join(absFilePath,'mountedDisk')
fKafkaRunCommand = os.path.join(absFilePath,'kafkaProduceRunCommand.py')
templatePushMDisk =  os.path.join(absFilePath,'templates','push-mountedDisk.xml')
templateExecKafkaRunCommand = os.path.join(absFilePath,'templates','executeProduceRunCommand.xml')

portJenkins = 8084
portKafka = 9092

####TENANT SPECIFIC#########
ipAddress = '172.20.0.1'
ipAddressJenkins = ipAddress
topic = 'vialis'
dMountedDiskHost = r"/home/rakip/Documents/projects/DSHTesting/mountedDisk"