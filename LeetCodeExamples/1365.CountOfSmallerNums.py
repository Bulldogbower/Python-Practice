import enum
count_list=[]

nums=[8,1,2,2,3,0]
for location, value in enumerate(nums):
    count=0
    for i in nums:
        if value>i:
            count=count+1
    count_list.append(count)
    if len(count_list)==len(nums):  
        print(count_list)



