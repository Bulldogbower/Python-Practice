n=5

binary_list=[]
count_list=[]

for i in range(n+1):
    binary_list.append(str(bin(i)[2:]))

for i in binary_list:
    count=0
    for i in str(i):
        if i =="1":
            count=count+1
    count_list.append(count)
print(count_list)
