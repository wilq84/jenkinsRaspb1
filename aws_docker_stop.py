import sys
import os
# jenkins exposes the workspace directory through env.
sys.path.append(os.environ['WORKSPACE'])
import boto3

ec2 = boto3.client('ec2')

docker_host = 'i-0f2f6efb6a43ad693'

#response = ec2.describe_instances()
#disable detail monitoring
response = ec2.monitor_instances(InstanceIds=[docker_host])
print(response)

response = ec2.stop_instances(InstanceIds=[docker_host], DryRun=False)
print(response)
