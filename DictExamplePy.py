import datetime
from operator import itemgetter

from dateutil.tz import tzlocal

list_1 = [
        {'id': '123-abc', 'name': 'Mike1', 'age': 40},
        {'id': '123-efg', 'name': 'John', 'age': 24},
        {'id': '123-xyz', 'name': 'Aly', 'age': 35}
    ]

list_2 = [
        {'id': 'abc', 'name': 'Mike', 'launch_time': datetime.datetime(2020,11, 17, 9,11,13, tzinfo=tzlocal())},
        {'id': 'def', 'name': 'Jon', 'launch_time': datetime.datetime(2021,11, 17, 9,11,13, tzinfo=tzlocal())},
        {'id': 'ghi', 'name': 'Aly', 'launch_time': datetime.datetime(2019,11, 17, 9,11,13, tzinfo=tzlocal())}
    ]
list4=[]

print(type(list4))

list3 = [{'1','2','3','4'}]
for i in list3:
    list4.append({"age": i, "address": 'NA', "job": 'NA'})
    #list4.append({"address": 'NA'})
    #list4.append({"job": 'NA'})
    #list4.__add__("age",i)
    #list4['ami_id'].append[i][0]
print(list4)


#for x in sorted(list_2, key=itemgetter('launch_time')):
    #print(x)
#def sortBySec(element):
#    return element[2]

#list_2.sort(key=sortBySec())

#def sortByKey():
#    sortbykeyDict = sorted(list_2.items(), key = lambda t: t[2])
#    print(sortbyKeyDict)

#print(list_2.sort(key=(lambda b: b.age())))

#for i in list_1:
 #   if i not in list_2:
  #      print(i)