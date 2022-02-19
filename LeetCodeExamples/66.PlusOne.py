digits=[1,2,3]
strings = [str(integer) for integer in digits]
a_string = "".join(strings)
an_integer = int(a_string)
an_integer=an_integer+1
backwards=[]

for i in str(an_integer):
    backwards.append(i)
print(backwards)
