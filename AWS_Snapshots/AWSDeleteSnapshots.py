import json
import boto3
from json import loads

ec2 = boto3.resource('ec2')
instances_id_ami = {}
for instance in ec2.instances.all():
    #instances_id_ami.append(instance[instance.id], instance.image.id)
    #print(
     #   "ID: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
    #    instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state)
    #)

    print("ID: {0}\nAMI: {1}\n".format(instance.id, instance.image.id))

    data = dict(loads(instance.id, instance.image.id))





#s3 = boto3.resource('s3')

#for bucket in s3.buckets.all():
 #     print (bucket.name)


