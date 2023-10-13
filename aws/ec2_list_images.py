import boto3

def main(args):
   ec2 = boto3.resource('ec2')
   for instance in ec2.instances.all():
      for tag in instance.tags:
         if tag['Key'] == 'Name':
            instanceName = tag['Value']      
      message = "Id: {0}\nType: {1}\nName: {2}\nAMI: {3}\nState: {4}\n".format(
         instance.id, 
         instance.instance_type, 
         instanceName, 
         instance.image.id, 
         instance.state
       )
      print(message)
   return 0

if __name__ == '__main__':
   import sys
   sys.exit(main(sys.argv))
