#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b)
prodReap=product(a,b,repeat=2)
print(list(prod))
print(list(prodReap))