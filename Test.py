import boto3
import os
from datetime import datetime

def get_session(region, access_id, secret_key):
    return boto3.session.Session(region_name=region,
                                 aws_access_key_id=access_id,
                                 aws_secret_access_key=secret_key)

def lambda_handler(event, context):
    session = get_session(os.getenv('REGION'),
                          os.getenv('ACCESS_KEY_ID'),
                          os.getenv('SECRET_KEY'))

    client = session.client('ec2')
    resource = session.resource('ec2')
    images = client.describe_images()
    for image_data in images['Images']:
        image= resource.Image(image_data['ImageId'])
        print ("image id", image)