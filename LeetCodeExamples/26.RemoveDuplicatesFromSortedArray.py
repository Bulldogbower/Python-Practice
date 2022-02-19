nums=[1,1,2]
unique=[]
length=len(nums)
print(length)
for i in nums:
    if i not in unique:
        unique.append(i)
unique_length=len(unique)
for i in nums:
    if len(unique) != length:
        unique.insert(len(nums)+1,"_")
nums=unique
print(nums)
print(unique)
print(unique_length)
#if nums.__contains__