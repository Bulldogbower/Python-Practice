#Open file for reading
f=open("National_Parks_Avaiability.txt")
#Read it line by line
lines=f.readlines()
converted_list = []
#To get rid of "\n"
for i in lines:
    converted_list.append(i.strip())
lines=converted_list
f.close()

#Sorting the months into seperate lists, starting with a string I hard coded "Month_x:$MONTH_NAME YYYY " 
for i in range(len(lines)):
    if lines[i].__contains__("Month_0"):
        a=int(i)
    if lines[i].__contains__("Month_1"):
        b=int(i)
    if lines[i].__contains__("Month_2"):
        c=int(i)
    if lines[i].__contains__("Month_3"):
        d=int(i)


#I accidentally created nested lists [[1,2,3],[4,5,6]]
month_0=[lines[a:b]]
#Quick way to fix it here. If you know of a better way then please show me
month_0=month_0[0]
month_1=[lines[b:c]]
month_1=month_1[0]
month_2=[lines[c:d]]
month_2=month_2[0]
month_3=[lines[d:]]
month_3=month_3[0]

#f=open("National_Parks_Avaiability.txt", "w")
f=open("output.txt", "w")

#Sort through each month individually, should be able to loop this, but that's a later problem
for i in range(len(month_0)):
    if month_0[i] == 'A':
        print(month_0[0], " has the ", month_0[i-1], " available")
        f.write(month_0[0], " has the ", month_0[i-1], " available" + "\n")
for i in range(len(month_1)):
    if month_1[i] == 'A':
        print(month_1[0], " has the ", month_1[i-1], " available")
        f.write(month_1[0], " has the ", month_1[i-1], " available" + "\n")
for i in range(len(month_2)):
    if month_2[i] == 'A':
        print(month_2[0], " has the ", month_2[i-1], " available")
        f.write(month_2[0], " has the ", month_2[i-1], " available" + "\n")
for i in range(len(month_3)):
    if month_3[i] == 'A':
        print(month_3[0], " has the ", month_3[i-1], " available")
        f.write(month_3[0] + " has the " + month_3[i-1] + " available" + "\n")




# flat_list = []
# for sublist in month_3:
#     for item in sublist:
#         flat_list.append(item)
# print(flat_list)









# for line in lines:
#     if line.__contains__("Month"):
#         print(line)