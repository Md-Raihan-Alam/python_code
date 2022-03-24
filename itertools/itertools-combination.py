#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import combinations,combinations_with_replacement
a=[1,2,3,4]
comb=combinations(a,2) #length is mandatory which is 2
print(list(comb))
comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))