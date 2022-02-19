import string
a="11"
b="1"
binary_total=[]
value=1
a_value=0
b_value=0

#10      9       8       7       6      5       4       3       2       1       0
#1024    512     256     128     64     32      16      8       4       2       1

for index, i in enumerate(a[::-1]): # 110 is enumerated as 011, 0 is index 0, 1 is index 1, 1 is index 2
    a_value=a_value+int(i)*2**index # each index value(0,1) is multiplied by it's index and raises by the power of two
                                    # 011 is: 0+0*0^2=0 0+1*1^2=2 2+1*2^2=6

for index, i in enumerate(b[::-1]):
    b_value=b_value+int(i)*2**index

t_value=a_value+b_value

list=range(0,11)
new_list=[]
for i in list:
    new_list.append(2**i)
#print(new_list)

for i in new_list[::-1]:
    remainder=t_value-i
    if remainder>=0:
        #print(remainder)
        remainder=remainder-i
        # if remainder>=0:
        #     print(remainder)

def PrintSomething(final_answer):
    print(final_answer)

def DecToBinary(t_value):
    print(t_value)
    remainder=t_value%2
    binary_total.append(remainder)
    t_value=int(t_value/2)
    print(t_value)
    if t_value==.5:
        print("Fuck yeah")
    if t_value>=1:
        print("Here")
        DecToBinary(t_value)
    else:
        final_answer=''.join(str(e) for e in binary_total[::-1])
        #print(str(final_answer))
        PrintSomething(final_answer)
DecToBinary(t_value)

