list1 = [11,12,13,14,1,2,3]
list2 = [11,1,2,12]

c = set(list1)
d = set(list2)
e=c.union(d)
f=c.intersection(d)
res = c.union(d)-c.intersection(d)
print("res", res)
