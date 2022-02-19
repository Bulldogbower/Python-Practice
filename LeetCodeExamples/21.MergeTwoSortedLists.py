list1=[1,2,4]
list2=[1,3,4]
list3=[]
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
list3.sort()
print(list3)