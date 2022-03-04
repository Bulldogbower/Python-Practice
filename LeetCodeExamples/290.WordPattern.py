pattern = "abba"
s = "dog cat cat dog"


s=s.split(" ")
pattern=list(pattern)

#print(pattern,s)

locations=[]

for location,value in enumerate(pattern):
    print(location,value)
    for i in pattern:
        if i in pattern[location+1:]:
            temp=pattern.index(i)+1
            #print(temp)
            print(pattern[temp:].index(i))