a = [1,2,4,2,1, 5,6,7,8,9,10]

b = [2,1,5,3,6,0, 55,9,10]

#c = [3,4,1,2,3,5,6]
#d = [3,4,7,8,9,11,12,13,14,1,2,88,99,111]
list1 = [{'snap-id': 'snap1234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snp3234', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snap9993', 'size': 'NA', 'snap_name': 'NA'},
      {'snap-id': 'snap4321', 'size': 'NA', 'snap_name': 'NA'},
       {'snap-id': 'snap8888', 'size': 'NA', 'snap_name': 'NA'}]
list2 = [{'snap-id': 'snap1234', 'size': '20', 'snap_name': 'abc'},
      {'snap-id': 'snp3234', 'size': '30', 'snap_name': 'def'},
      {'snap-id': 'snap9993', 'size': '40', 'snap_name': 'ght'},
      {'snap-id': 'snap1222', 'size': 'NA', 'snap_name': ''},
      {'snap-id': 'snp3239', 'size': 'NA', 'snap_name': ''},
      {'snap-id': 'snap9963', 'size': 'NA', 'snap_name': ''}]

res = []
diff = []

rest1=[]
for d2 in list1:
    found_flag = 0
    for d1 in list2:
        if d2['snap-id'] == d1['snap-id']:
            res.append(d2)
            boo_result = 1
            break
        elif d2['snap-id'] != d1['snap-id']:
            rest1.append(d2)
            boo_result = 1
            break
        if found_flag == 0:
                diff.append(d2)
print("rest", res)
print("not matching value 2", rest1)
print("\n")
#print("diff", diff)
#print("remainig matching id", rest1)
#print("difference of result",diff)