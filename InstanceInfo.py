from collections import defaultdict
import boto3

ec2 = boto3.resource('ec2')

running_instances = ec2.instances.all()

ec2_info = defaultdict()

for instance in running_instances:
    for tag in instance.tags:
        if 'Name' in tag['Key']:
            name = tag['Value']
    ec2_info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'ImageId': instance.Image_Id ###########Need to look into Image id####
    }

    attributes = ['Name', 'Type', 'ImageId']

    for instance_id, instance in ec2_info.items():
        for key in attributes:
            print("{0}: {1}: {2}".format(key, instance[key]))
            print("-------")
