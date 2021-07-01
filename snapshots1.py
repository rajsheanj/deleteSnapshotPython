import boto3
import json


l1 = [{'ami_id': 'ami-of30', 'ami_name': 'BASE-AMI', 'platform': 'windows', 'age': 30},
      {'ami_id': 'ami-0f50', 'ami_name': '', 'platform': 'linux', 'age': 90 },
      {'ami_id': 'ami-of43', 'ami_name': 'BASE-no', 'platform': 'windows', 'age': 110}]
snapl2 = [{'ami_id': 'ami-of30', 'ami_name': 'NA', 'platform': 'NA'},
      {'ami_id': 'ami-0f50', 'ami_name': 'NA', 'platform': 'NA'},
      {'ami_id': 'ami-of43', 'ami_name': 'NA', 'platform': 'NA'}, {'ami_id': 'ami-1234', 'ami_name': 'NA', 'platform': 'NA'}]

'''t1 = set(l1)
t2 = set(snapl2)
t_f = t1.union(t2)
final = t1.union(t2) - t1.intersection(t2)
#print(final) '''

list1_final = [{'snap-id': 'snap1234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snp3234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snap9993', 'size': 'NA', 'snap_name': 'NA'}]

list2_all = [{'snap-id': 'snap1234', 'size': '20', 'snap_name': 'abc'},
      {'snap-id': 'snp3234', 'size': '30', 'snap_name': 'def'},
      {'snap-id': 'snap9993', 'size': '40', 'snap_name': 'ght'},
      {'snap-id': 'snap1222', 'size': 'NA', 'snap_name': ' '},
      {'snap-id': 'snp3239', 'size': 'NA', 'snap_name': ' '},
      {'snap-id': 'snap9963', 'size': 'NA', 'snap_name': ' '}]

matchingArr = map(list, set(map(tuple, list1_final)).intersection(set(map(tuple, list2_all))))
notMatchingArr = map(list, set(map(tuple, list1_final)).difference(set(map(tuple, list2_all))))
print(matchingArr)
print(notMatchingArr)
for ii in matchingArr:
    print(ii)

for jj in notMatchingArr:
    print(jj)

checkNameSet = set(map(tuple, list2_all))
#checkNameSet2 = set(map(tuple, list1_final))
found = []
notfound = []
for i in list1_final:
    if tuple(i) in checkNameSet:
        found.append(i)
    else:
        notfound.append(i)

print("found###", found)
print("not fould##", notfound)
#print("final result", i)

#json_obj = json.dumps(l2)
#print(json_obj)
#print("list1", json_obj2)
# initializing compare keys
comp_keys = ['snap-id']
fff =[]
#for k in comp_keys:
#    if l1.get(k) == l2.get(k):
#        fff.append(l2.append())



#for kk in i1.values():







