import os
from os.path import expanduser

home = expanduser("~")
topic = 'vialis'
#pLogo = os.path.join('/home/rakeshlaptop/Documents/dockerRF/DSH-Jenkins2','vialis.png')

absFilePath = os.path.dirname(os.path.abspath(__file__))
dMountedDisk = os.path.join(os.path.dirname(os.path.dirname(absFilePath)),'mountedDisk')
fKafkaRunCommand = os.path.join(os.path.dirname(absFilePath),'kafkaProduceRunCommand.py')
templatePushMDisk =  os.path.join(os.path.dirname(absFilePath),'templates','push-mountedDisk.xml')
templateExecKafkaRunCommand = os.path.join(os.path.dirname(absFilePath),'templates','executeProduceRunCommand.xml')
