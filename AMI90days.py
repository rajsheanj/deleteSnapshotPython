import boto3
import logging
from dateutil.parser import parse
import datetime
age = 90
#aws_profile_name = 'dev'
list_ami_id =[]
print("entry first zero")
def days_old(date):
    get_date_obj = parse(date)
    date_obj = get_date_obj.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

#boto3.setup_default_session(profile_name = aws_profile_name)
print("entry here")
ec2 = boto3.client('ec2')
amis = ec2.describe_images(Owners=['self'])
for ami in amis['Images']:
    create_date = ami['CreationDate']
    ami_id = ami['ImageId']
    # print ami['ImageId'], ami['CreationDate']
    day_old = days_old(create_date)
    print("day old", day_old)
    if day_old < age:
        print("enter inside..")
        list_ami_id.append(ami['ImageId'])
        #print("Deleting -> " + ami_id + " - create_date = " + create_date)
        #print "deleting -> " + ami_id + " - create_date = " + create_date
        # deregister the AMI
        #ec2.deregister_image(ImageId=ami_id)

print("list of ami id", list_ami_id)