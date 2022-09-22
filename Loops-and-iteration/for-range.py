nums=[1,3,4,5,6,3,5,7,0,8,7,3,2,1,2,3,4,7,8,1,2,5]
#for loop for range
for i in range(len(nums)):
    print(nums[i])
# double loop
        #range(limit)
        #range(start,limit)
        #range(start,limit,incr)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            print(nums[j])
