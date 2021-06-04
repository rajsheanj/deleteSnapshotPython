a = [1,2,4,2,1, 5,6,7,8,9,10]

b = [2,1,5,3,6,0, 55,9,10]





c = [3,4,1,2,3,5,6]
d = [3,4,7,8,9,11,12,13,14,1,2,88,99,111]

e =[]

cc=set(c)
dd=set(d)
#f= cc.union(dd)
#g=cc.intersection(dd)
h=cc.union(dd)-cc.intersection(dd)
#print("union value",f)
#print("intersection value",g)
print("Result",h)
