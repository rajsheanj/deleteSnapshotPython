list1 = [
    {'snap-id': 'snap1234', 'size': 'NA', 'snapname': 'NA'},
    {'snap-id':'snp3234', 'size': 'NA', 'snapname': 'NA'},
    {'snap-id': 'snap9993', 'size': 'NA', 'snapname': 'NA'}
     ]

list2 = [
    {'snap-id': 'snap1234', 'size': '20', 'snapname': 'abc'},
    {'snap-id': 'snp3234', 'size': '30', 'snapname': 'def'},
    {'snap-id': 'snap9993', 'size': '40', 'snapname': 'ght'},
    {'snap-id': 'snap1222', 'size': 'NA', 'snapname': ' '},
    {'snap-id': 'snp3239', 'size': 'NA', 'snapname': ' '},
    {'snap-id': 'snap9963', 'size': 'NA', 'snapname': ' '}
]

list3 = []
list4 = []
list5 = []
list3 = []
for i in list2:
    for j in list2:
        if i['snap-id'] == j['snap-id']:
            list3.append(j)
            break
        else:
            list4.append(i)
            break

print(list3)
#print(list4)
