#a=[1,2,3,4,5,11]
#b=[9,8,7,6,5,10,11,1,1]

#same_values = set(a) & set(b)
#print("output", same_values)

list1 = [{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30},
{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30},
{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30},
{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30}]

re = list(set(list1))

print(re)



l1 = [{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30},{'ami_id': 'ami-0f50', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 90 },{'ami_id': 'ami-of43', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 110}]
l2 = [[{'ami_id': 'ami-9876', 'ami_name': 'BASE-kum', 'platform': 'lin'},{'ami_id': 'ami-1234', 'ami_name': 'BASE-raj', 'platform': 'ubuntu'},{'ami_id': 'ami-5678', 'ami_name': 'BASE-AMI', 'platform': 'windows'}]]

l3 = l1 + l2
#print(l3)

''''l1 = []
for i in l:
    for i in l2:
        if i not in l2:
            #if i in l1:
            l1.append(i)
#print(l1) '''

