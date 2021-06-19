
emailbody = "welcome to mail"

sendmail = "Instance Name   \t  InstanceID  \t      ami_id  \t  launch_time \t"
print (sendmail)

list1 = [{"instanceName": 'rajkumar', "instance_id": '0343433', "ami_id":'12345'}]
#s = len(list)
#email_body= "length is ", s

#email_body = email_body + "please find out the list of instances..."
#print(email_body)
result = "Ami lists"
for item in list1:
    print(":", item, " " *(9 - len(item)), ":",
          item, " " *(13 - len(item)), ":",
          item, " " *(4 - len(item)), ":", )
    #result = sendmail +"\n" + i['instanceName']   + "\t" + i['instance_id'] +"\t"     + i['ami_id']+ "\t"
    #result = ":" + result + "\t" + i['instanceName'] + "\t"

#print("result \033[1m", result)


