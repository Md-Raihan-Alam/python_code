from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=2
print(d)
print(d['a'])
print(d['b'])
print(d['c']) # outuput default value
d2=defaultdict(float)
d2['a']=1
d2['b']=2
print(d2)
print(d2['a'])
print(d2['b'])
print(d2['c']) # outuput default value