mySet=set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.remove(2)
print(mySet)
mySet.discard(1)
print(mySet)
mySet.discard(1) # will not cause error but remove will