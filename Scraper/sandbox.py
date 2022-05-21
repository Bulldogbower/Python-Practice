f=open("National_Parks_Avaiability.txt")
lines=f.readlines()
print(lines)

f2=open("comparison.txt")
lines2=f2.readlines()
print(lines2)

if lines==lines2:
    print("No update at this time")
else:
    f2=open("comparison.txt", "w")
    print("Update found, send email")
    for i in lines:
        f2.write(str(i))