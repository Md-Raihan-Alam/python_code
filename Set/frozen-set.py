#frozen sets are immutable
a=frozenset([1,2,3,4,5])
# a.add(6) will cause error
# a.remove(1) will cause error
print(a)