a = [1,2,4,2,1, 5,6,7,8,9,10]

b = [2,1,5,3,6,0, 55,9,10]

#c = [3,4,1,2,3,5,6]
#d = [3,4,7,8,9,11,12,13,14,1,2,88,99,111]
list1 = [{'snap-id': 'snap1234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snp3234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snap9993', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snap4321', 'size': 'NA', 'snap_name': 'NA'},
         {'snap-id': 'snap2222', 'size': 'NA', 'snap_name': 'NA'}]
list2 = [{'snap-id': 'snap1234', 'size': '20', 'snap_name': 'abc'},
      {'snap-id': 'snp3234', 'size': '30', 'snap_name': 'def'},
      {'snap-id': 'snap9993', 'size': '40', 'snap_name': 'ght'},
      {'snap-id': 'snap1222', 'size': 'NA', 'snap_name': ''},
      {'snap-id': 'snp3239', 'size': 'NA', 'snap_name': ''},
      {'snap-id': 'snap9993', 'size': 'NA', 'snap_name': ''},
      {'snap-id': 'snap4321', 'size': 'NA', 'snap_name': ''}]

res = []
list3 = []

rest1=[]
for d1 in list1:
    found_flag = 0
    for d2 in list2:
        if d1['snap-id'] == d2['snap-id']:
            res.append(d2)
            found_flag = 1
            break
    if found_flag == 0:
        list3.append(d1)
print("rest", res)
print("list3", list3)
print("\n")
#print("diff", diff)
#print("remainig matching id", rest1)
#print("difference of result",diff)