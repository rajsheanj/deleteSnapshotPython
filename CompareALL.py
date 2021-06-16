import boto3
import json
import logging
from dateutil.parser import parse
import datetime
age = 90
list_ami_id =[]
list_of_instance_amis = []
list_of_instance = []
list_if_amis = []
#aws_profile_name = 'dev'
def days_old(date):
    get_date_obj = parse(date)
    date_obj = get_date_obj.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

#boto3.setup_default_session(profile_name = aws_profile_name)
ec2 = boto3.client('ec2')
ec2_res = boto3.resource('ec2', 'us-east-1')
amis = ec2.describe_images(Owners=['self'])
for inst_detail in ec2_res.instances.all():
    list_of_instance_amis.append({'instanceName': inst_detail.instance_id, 'ImageID': inst_detail.image_id})
    list_of_instance.append(inst_detail.instance_id)
    list_if_amis.append(inst_detail.image_id)
print("instance name", list_of_instance)
print("ami ID", list_if_amis)
#json_string = json.dumps(list_of_instance_amis)

for ami in amis['Images']:
    create_date = ami['CreationDate']
    ami_id = ami['ImageId']
    # print ami['ImageId'], ami['CreationDate']
    day_old = days_old(create_date)
    if day_old < age:
        print("Old date and ami_id", day_old, ami_id, create_date)
        list_ami_id.append(ami['ImageId'])
        print("length", len(list_ami_id))
        ##print("Deleting -> " + ami_id + " - create_date = " + create_date)
        #print "deleting -> " + ami_id + " - create_date = " + create_date
        # deregister the AMI
        #ec2.deregister_image(ImageId=ami_id)

#temp1 = set(list_of_instance_amis)
#temp2 = set(list_ami_id)
#list_of_final_amis = temp1.union(temp2)-temp1.intersection(temp2)
instancesName = []
for i in ec2_res.instances.all():
    for tag in i.tags:
        if tag['Key'] == 'Name':
            instancesName.append({'instanceName': tag['Value'], 'ami_id': i.image_id, "launch_time": i.launch_time})
            print("tag name", tag['Value'])
print("instancesDetail##",instancesName)

result = []
#for inst_detail in ec2_res.instances.all():
#    for i in list_ami_id:
#        if (i in inst_detail.image_id):
#            for tag in inst_detail.tags:
#                print(tag['Value'])
#                result.append({'instanceName': tag['Value'],'instanceID': inst_detail.instance_id, 'ami_id': inst_detail.image_id})
#                print("resukta", result)