arr1=[1,1,1,1,1]
arr2=[1,0,1]

arr1=[0]
arr2=[1,0]

arr1=[0]
arr2=[1,0]

arr1_value=0
arr2_value=0
for location, value in enumerate(arr1[::-1]):
    #print(location,value)
    if value==1:
        #print("-2^",location, " = ", ((-2)**int(location)))
        arr1_value=arr1_value+((-2)**int(location))
#print(arr1_value)
for location, value in enumerate(arr2[::-1]):
    #print(location,value)
    if value==1:
        #print("-2^",location, " = ", ((-2)**int(location)))
        arr2_value=arr2_value+((-2)**int(location))
total=arr1_value+arr2_value
print(total)
print(bin(total))
binary_total=[]
if total==0:
    print(0)
if total>0:
    binary_total=bin(total)[2:]
temp=0
binary_temp=[]
if total<0:
    for i in range(int(total))[::-1]:
        temp=temp+(-2)**i
        print(temp,total)
        binary_temp.append("1")
        if temp==total:
            break
print(binary_temp)
print(binary_total)

#return(int(arr1_value+arr2_value))