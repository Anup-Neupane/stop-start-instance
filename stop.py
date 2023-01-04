import boto3
region = 'us-west-1'
instances = ['i-085f73348c86af8c9', 'i-043b6d1d9c733649']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
