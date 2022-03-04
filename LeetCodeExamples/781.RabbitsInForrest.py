answers=[0,0,1,1,1]
unique=[]
value=0
for i in answers:
    unique.append(i+1)
print(unique)
for i in unique:
    value=value+i
if value>len(answers):
    print(value)
else:
    print(len(answers))