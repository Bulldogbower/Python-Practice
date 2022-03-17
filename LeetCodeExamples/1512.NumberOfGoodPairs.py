nums = [1,2,3,1,1,3]
count=0
for location, value in enumerate(nums):
    for i in range(len(nums)):
        if nums[i] == value and i != location:
            #print(location, i)
            count=count+1
print(int(count/2))