from operator import itemgetter

list1 = [{'id': 'ami-07656', 'name': 'raj', 'office': 'chennai', 'pincode': '600201', 'age': '88'}, {'id': 'ami-0123654', 'name': 'rajkumar', 'office': 'madurai', 'pincode': '600201', 'age': '88'}, {'id': '123', 'name': 'xxddfdf', 'office': 'orisa','pincode': '600201', 'age': '88'}]
list2 = [{'id': 'ami-07656', 'address': 'kannapannamgar', 'platform': 'windows'}, {'id': '123', 'address': 'kannapannamgar', 'platform': 'windows'}, {'id': '124', 'address': 'kannapannamgar', 'platform': 'windows'}]
#list3 = [{'id': 'ami-07656', 'name':'', 'office': ''},{ 'id': 'ami-0123654', 'name': '', 'office': ''}]
list3 = [{'id': 'ami-07656', 'id': 'ami-0123654'}]


#list1, list3 = [sorted(l, key=itemgetter('id')) for l in (list1, list3)]
#print("list 1 and list 2", list1, list3)

#def new_change(old_list, new_list):
change_list = []
for x in list1:
    for y in list3:
        if x['id'] != y['id']:
            print("inside the if loop...")
            print("name and office", x['name'], x['office'])
            change_list.append(x['id'])
            change_list.append(x['name'])
            change_list.append(x['office'])
print("changelist", change_list)
   ##return change_list

for i in list2:
    for j in list3:
        if i['id'] == j['id']:

            print("inside the if loop...")
            print("name and office", i['address'], i['platform'])
            change_list.append(i['id'])
            change_list.append(i['address'])
            change_list.append(i['platform'])
            change_list.append({'id': i['id'], 'address': i['address'], 'platform': i['platform']})

print("final list name, office, addressh , platform ", change_list)
