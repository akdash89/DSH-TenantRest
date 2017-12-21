import os
from os.path import expanduser

home = expanduser("~")
topic = 'vialis'
pLogo = os.path.join('/home/rakeshlaptop/Documents/dockerRF/DSH-Jenkins2','vialis.png')
dMountedDisk = os.path.join(home, 'Documents', 'dockerRF', 'mountedDisk')
templatePushMDisk = os.path.join('/home/rakeshlaptop/Documents/dockerRF/DSH-Jenkins2/configs','push-mountedDisk.xml')
templateExecKafkaRunCommand = os.path.join('/home/rakeshlaptop/Documents/dockerRF/DSH-Jenkins2/configs','executeProduceRunCommand.xml')
fKafkaRunCommand = os.path.join('/home/rakeshlaptop/Documents/dockerRF/DSH-kafka', 'kafkaProduceRunCommand.py')
