import boto3

def describe_ec2_instances():
    try:
        print("Desc EC2 instances")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances())
        #resource_ec2.run_instances(ImageId='ami-04d29b6f966df1537')
        #print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])

    except Exception as e:
        print(e)

describe_ec2_instances()