from kafka import KafkaProducer
import json
import sys


def main(args):
  if (len(args) != 5):
    usage(args)
  else: 
    print("About to produce a message to: " + args[1] + ":" + args[2] + ", topic: " + args[3])    
    try:
      producer = KafkaProducer(bootstrap_servers=args[1] + ":" + args[2],
                                value_serializer=lambda v: bytes(v, "utf-8"),
                                acks='all',
                                retries = 3)      
      message = open(args[4], "r")  
      producer.send(args[3], message.read())
    except:
      print("Unexpected exception: ",sys.exc_info()[0])
  return 0
    

def usage(args):
  print('python ' + args[0]+ ' <server> <port> <topic> <file to post>')


if __name__ == '__main__':
  sys.exit(main(sys.argv))
