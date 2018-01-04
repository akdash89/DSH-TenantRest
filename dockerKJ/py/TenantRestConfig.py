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
ipAddress = 'IPADDRESS'
ipAddressJenkins = ipAddress
topic = 'TOPIC'
dMountedDiskHost = r"PATHTOMOUNTEDDISK"