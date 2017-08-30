import sys
sys.path.append('/usr/local/aws/lib/python2.7/site-packages')

import boto3
import json

client = boto3.client('kinesis', 'cn-north-1')

# get iterator
iterator = client.get_shard_iterator(
    StreamName='mystream',
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST'
#    StartingSequenceNumber = '49553137180157178225565789151570069030202712349493690386'
) 

print iterator['ShardIterator']

response = client.get_records(
    ShardIterator = iterator['ShardIterator'],
    Limit=123
)

print response
#print json.dumps(response,indent=4)
