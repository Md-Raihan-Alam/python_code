#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import groupby
persons=[{'name':'Tim','age':25},{'name':'Don','age':25},
        {'name':'Lisa','age':26},{'name':'Clair','age':20}]
group_obj=groupby(persons,key=lambda x:x['age'])
for key,value in group_obj:
    print(key,list(value))