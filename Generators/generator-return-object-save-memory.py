import sys
def firstn_generator(n):
    num=0
    while num<n:
        yield num
        num+=1
def firstn_n(n):
    nums=[]
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

print(sum(firstn_generator(1000000)))
print(sum(firstn_n(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
print(sys.getsizeof(firstn_n(1000000)))