import boto3
import pprint
import sys
import time
import datetime

client = boto3.client('ec2', region_name='us-east-1')
snapshots = client.describe_snapshots(OwnerIds=['399173713737'])

snap_list = []
for snap_detail in snapshots['Snapshots']:
    snap_list.append(snap_detail['SnapshotId'])

print("available snaphosts", len(snap_list))

amilist = client.describe_images(Owners=['399173713737'], DryRun=False)

img_snap = []

for image_deta in amilist['Images']:
    for blockmap in image_deta['BlockDeviceMappings']:
        try:
            img_snap.append(blockmap['Ebs']['SnapshotId'])
        except:
            break

for x in img_snap:
    snap_list.remove()

print("snapshots without ami= {}", len(snap_list))

