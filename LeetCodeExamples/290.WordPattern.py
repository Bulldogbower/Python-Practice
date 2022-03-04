pattern = "abba"
s = "dog cat cat dog"


s=s.split(" ")
pattern=list(pattern)

#print(pattern,s)
temp=[]
locations=[]
match_count=0
ps=set(pattern)



