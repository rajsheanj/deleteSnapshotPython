#a=[1,2,3,4,5,11]
#b=[9,8,7,6,5,10,11,1,1]

#same_values = set(a) & set(b)
#print("output", same_values)


l = [1,2,3,4,5,6,7,9,5,2,3,4]
l2 = [5,6,7,8,9,11,12,13,14,15]

l1 = []
for i in l:
    if i not in l2:
        if i not in l1:
            l1.append(i)
    else:
        print("", i)
