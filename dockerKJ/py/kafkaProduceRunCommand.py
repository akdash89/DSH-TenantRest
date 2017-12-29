import argparse
import time
 
from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError

parser = argparse.ArgumentParser()  
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("--run", "-r", help="give kafka produce run command")

# read arguments from the command line
args = parser.parse_args() 
 
def print_response(response=None):
    if response:
        print('Error: {0}'.format(response[0].error))
        print('Offset: {0}'.format(response[0].offset))
 
 
def main():
    # check for --version or -V
    if args.version:  
        print("Ask rakesh.partapsing@kpn.com")

    if args.run:  
        
        topic = args.run.split('/')[0]
        msg = bytes('RUN ' + str(args.run.split('/')[1]), 'utf8')
        
        kafka = KafkaClient("127.0.0.1:9092")
        producer = SimpleProducer(kafka)
        
        kafka.ensure_topic_exists(topic)
     
        try:
            print_response(producer.send_messages(topic, msg))
        except LeaderNotAvailableError:
            time.sleep(1)
            print_response(producer.send_messages(topic, msg))
     
        kafka.close()
 
if __name__ == "__main__":
    main()