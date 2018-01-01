import os
from os.path import expanduser

home = expanduser("~")

absFilePath = os.path.dirname(os.path.abspath(__file__))
dMountedDisk = os.path.join(os.path.dirname(os.path.dirname(absFilePath)),'mountedDisk')
fKafkaRunCommand = os.path.join(absFilePath,'kafkaProduceRunCommand.py')
templatePushMDisk =  os.path.join(os.path.dirname(absFilePath),'templates','push-mountedDisk.xml')
templateExecKafkaRunCommand = os.path.join(os.path.dirname(absFilePath),'templates','executeProduceRunCommand.xml')
kafkaServer = '172.22.0.1:9092'
