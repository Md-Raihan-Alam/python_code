import sys
mygenerator=(i for i in range(100000) if i %2==0)
print(sys.getsizeof(mygenerator))
mygeneratorList=[i for i in range(100000) if i %2==0]
print(sys.getsizeof(mygeneratorList))