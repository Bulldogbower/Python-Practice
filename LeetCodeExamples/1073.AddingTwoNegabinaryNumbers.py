arr1=[1,1,1,1,1]
arr2=[1,0,1]

arr1=[0]
arr2=[1,0] #[1,0]

arr1=[0]
arr2=[1,1] #[1,1]

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
temp=0
print(total)
bin_lst=[]
print(total)
for location, value in enumerate(range(len(max(arr1,arr2)))[::-1]):
    print(location,value)  

print(bin_lst)
bin_lst=bin_lst[::-1]
#print(bin_lst[bin_lst.index(1):])
#return(int(arr1_value+arr2_value))