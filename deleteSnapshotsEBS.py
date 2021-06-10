import json
import boto3
import pprint
import sys
import time
import datetime

def ebsvol():
    c = boto3.client('ec2','us-east-1')
    snapshots = c.describe_snapshots()
    snapshots_list = []
    for snapshots_detail in snapshots['Snapshots']:
         snapshots_list.append(snapshots_detail['SnapshotId'])
    print("no of snaphsots", snapshots)
    ami_list = c.describe_image()
    image_snapshots =[]
    for image_detail in ami_list['Images']:
        for blockmap in image_detail['BlockDeviceMappings']:
            try:
                image_snapshots.append(blockmap['Ebs']['SnapshotId'])
            except:
                break
    print("Number of snapshots used by AMI {}".format(len(image_snapshots)))
ebsvol()