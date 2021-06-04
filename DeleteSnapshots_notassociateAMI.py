import boto3
import datetime
import logging

logger = logging.getLogger("Snapshots Deletion")
logger.setLevel(logging.INFO)
client = boto3.client('ec2', region_name='us-east-1')
snapshots = client.describe_snapshots(OwnerIds=['399173713737'])
for snapshot in snapshots['Snapshots']:
    a = snapshot['StartTime']
    b = a.date()
    c = datetime.datetime.now().date()
    d = c - b
    try:
        if d.days >= 1:
            id = snapshot['SnapshotId']
            print("Deleted Snapshots . . . ", id)
            client.delete_snapshot(SnapshotId=id)
    except Exception as ex:
        if 'InvalidSnapshot.InUse' in ex:
            logger.info("Skipping the Snapshots" + str (ex))
            #print("skipping this snapshot", ex.message)
            continue