#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import permutations
a=[1,2,3]
# return all possible ordering
perm=permutations(a)
permLen=permutations(a,2) # only 2 length
print(list(perm))
print(list(permLen))