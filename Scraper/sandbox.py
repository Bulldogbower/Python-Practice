f=open("National_Parks_Avaiability.txt")
lines=f.readlines()
#print(len(lines))
converted_list = []
for i in lines:
    converted_list.append(i.strip())
lines=converted_list
print(lines)


#Find "Month x"



for i in range(len(lines)):
    if lines[i].__contains__("Month 0"):
        a=int(i)
    if lines[i].__contains__("Month 1"):
        b=int(i)
    if lines[i].__contains__("Month 2"):
        c=int(i)
    if lines[i].__contains__("Month 3"):
        d=int(i)
    if lines[i].__contains__("Month 4"):
        e=int(i)



print(lines[a])
month_0=[lines[a:b-1]]
month_1=[lines[b:]]
month_2=[]
month_3=[]

# month_0 = month_0.strip()
print(month_0)
print(month_1)


# for line in lines:
#     if line.__contains__("Month"):
#         print(line)