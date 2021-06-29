list1_final = [{'snap-id': 'snap1234', 'size': 'NA', 'snapname': 'NA'},
               {'snap-id': 'snp3234', 'size': 'NA', 'snapname': 'NA'},
               {'snap-id': 'snap9993', 'size': 'NA', 'snapname': 'NA'},
               {'snap-id': 'snap1111', 'size': 'NA', 'snapname': 'NA'}]

list2_all = [{'snap-id': 'snap1234', 'size': '20', 'snapname': 'abc'},
             {'snap-id': 'snp3234', 'size': '30', 'snapname': 'def'},
             {'snap-id': 'snap9993', 'size': '40', 'snapname': 'ght'},
             {'snap-id': 'snap1222', 'size': 'NA', 'snapname': ' '},
             {'snap-id': 'snp3239', 'size': 'NA', 'snapname': ' '},
             {'snap-id': 'snap9963', 'size': 'NA', 'snapname': ' '}]

# make helper dict from list2_all with 'snap-id' values as keys, dicts as values
d = {v['snap-id']: v for v in list2_all}
out = []
for x in list1_final:
    y = d.get(x['snap-id'], None)
    if y is not None:
        out.append(y)
print(out)