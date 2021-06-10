test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
list = [{"name": "rajkumar", "age": "10", "address": "madurai"},{"name": "shen", "age": "30", "address": "srivilli"}]

list2 =[{"name": "rajkumar", "name": "rajkumar2", "name": "rajkumar3", "name": "rajkumar4", "name": "rajkumar5", "name":"rajkumar6"}]
compare_list=[]
for i in list:
    for i in list2:
        if i[name] == i[name]
            print(i)

#for i in list:
#    print(i["name"])
#    print(i["age"])
 #   print(i["address"])
# printing original dictionary
#print("The original dictionary is : " + str(test_dict))

# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

# printing result
print("The dictionary after values removal : " + str(res))