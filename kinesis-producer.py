import sys
sys.path.append('/usr/local/aws/lib/python2.7/site-packages')

import boto3
import json

client = boto3.client('kinesis', 'cn-north-1')

# put records

for i in range(0,100000):

  message = 'Putting %s' % (i)
  print message
  response = client.put_record(
      StreamName='mystream',
      Data=str(i),
      PartitionKey='test'
  )

  print response


