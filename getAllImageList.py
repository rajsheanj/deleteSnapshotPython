import boto3
import json

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["ImageId"])

#ec2_client = boto3.client('ec2', region_name='us-east-1') # Change as appropriate

#images = ec2_client.describe_images(Owners=['399173713737'])

#print(images)

#for i in images[images]:
#    ami_id = i['ImageId']
#    print("Image id..", ami_id)