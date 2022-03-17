num=2932

num=str(num)
num1=num[0:2]
num2=num[2:4]
number1=[]
number1.append(num1)
number1.append(num1[::-1])
number1=min(number1)
number2=[]
number2.append(num2)
number2.append(num2[::-1])
number2=min(number2)
#print(number1,number2)

num3=num[0]+num[3]

num4=num[1]+num[2]
#print(num3, num4)

number3=[]
number3.append(num3)
number3.append(num3[::-1])
number3=min(number3)
number4=[]
number4.append(num4)
number4.append(num4[::-1])
number4=min(number4)
#print(number3,number4)
final_num1=int(number1)+int(number2)
final_num2=int(number3)+int(number4)
result=[]
result.append(final_num1)
result.append(final_num2)
print(min(result))



#print(int(number1)+int(number2))