import boto3
import pprint
import sys
import time
import datetime

pp = pprint.PrettyPrinter(indent=4)

print("I am starting!")
client = boto3.client('ec2',region_name='us-east-1')
snapshots = client.describe_snapshots(OwnerIds=['399173713737'])

snapshot_list = []
for snapshot_detail in snapshots['Snapshots']:
    snapshot_list.append(snapshot_detail['SnapshotId'])
print(snapshot_list)
print("Number of available snapshots {}".format(len(snapshot_list)))
print("Starting ami lookup")
# get a list of ami
ami_list = client.describe_images(
    Owners=[
        '299576226671',
    ],
    DryRun=False
)

images_snapshots = []
for image_detail in ami_list['Images']:
    for blockmap in image_detail['BlockDeviceMappings']:
        try:
            images_snapshots.append(blockmap['Ebs']['SnapshotId'])
        except:
            break

print("Number of snapshots used by AMI {}".format(len(images_snapshots)))

print("time to cross check")

for x in images_snapshots:
    snapshot_list.remove(x)

print("snapshot without any ami = {}".format(len(snapshot_list)))
pp.pprint(snapshot_list)