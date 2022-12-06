import boto3

def main(args):
   s3 = boto3.client('s3')
   response = s3.list_buckets()
   print(response)
   return 0

if __name__ == '__main__':
   import sys
   sys.exit(main(sys.argv))
