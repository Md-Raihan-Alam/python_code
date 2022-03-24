#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import count,cycle,repeat
a=[1,2,3]
for i in count(10):
    print(i)
    if i==100:
        break

for i in cycle(a):
    print(i)

for i in repeat(1,100):# repeat only 100 if none then infinte
    print(i)