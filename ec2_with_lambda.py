import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance = ec2.create_instance(
        ImageID = AMI,
        Instance_Type = INSTANCE_TYPE,
        Key_Name = KEY_NAME,
        Subnet_Id = SUBNET_ID,
        MaxCount = 1,
        MinCount = 1
    )

    print("New instance Created: ", instance[0].id)