import boto3
import json

list_of_instance=[]
list_of_Amis=[]

ec2 = boto3.client('ec2')
amis = ec2.describe_images()
#ec2_response = boto3.resource('ec2', 'us-east-1')
#for inst_details in ec2_response.instances.all():
#      list_of_Amis.append({'instanceName': inst_details.instance_id, 'img_id': inst_details.image_id})
   #entry = {'instanceName': inst_details.instance_id, 'img_id': inst_details.image_id}
#      print(inst_details.instance_id, inst_details.image_id)
   #entry = {'instanceName': inst_details.instance_id, 'img_id': inst_details.image_id}
#print(list_of_Amis)
for ami in amis['Images']:
      create_date = ami['CreationDate']
      ami_id = ami['ImageId']
      print(ami_id)
   #json_obj = json.dumps(entry)
   #print(json_obj)

### WORKING NEED TO INVESTIGATE


   #list_of_Amis.append("instanceID", inst_details.instance_id)

   #list_of_instance.append(inst_details.instance_id)
   #list_of_Amis.append(inst_details.image_id)

   #.dumps(list_of_instance)
   #print('list of amis', list_of_Amis)


    #list_of_instance.append(inst_details.instance_id, inst_details['ImageId'])

#print(list_of_instance)

#print(list_of_Amis)


