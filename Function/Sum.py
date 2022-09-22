# sum(iterable, start)  default is 0
numbers = [1,2,3,4,5,1,4,5]
 
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
 
# start = 10
Sum = sum(numbers, 10)
print(Sum)

# with a list
nums=[10,20,30,40,50]
Sum=sum(nums[i] for i in range(len(nums)))
print(Sum)