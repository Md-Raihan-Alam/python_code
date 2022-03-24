#itertools: product,permutation,combination,accumlate,groupby and infinite interators
from itertools import accumulate
import operator
a=[1,2,5,3,4]
acc=accumulate(a)
accmul=accumulate(a,func=operator.mul)
accmax=accumulate(a,func=max)
#2nd(list one) with 1st(list two)
print(a)
print(list(acc)) 
print(list(accmul))
print(list(accmax))