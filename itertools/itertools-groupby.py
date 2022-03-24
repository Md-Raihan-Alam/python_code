#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import groupby
def smaller_than_3(x):
    return x<3
a=[1,2,3,4,5]
groupby_obj=groupby(a,key=smaller_than_3)
print(groupby_obj)
for key,value in groupby_obj:
    print(key,list(value))