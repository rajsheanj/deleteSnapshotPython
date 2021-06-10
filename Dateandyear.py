from datetime import date
a = date(2017,6,8)
b = date.today()
d= (a-b).days
s= str(d)
f = s.replace("-", "")
print(f)
#print(d)
#print((a-b).days)

