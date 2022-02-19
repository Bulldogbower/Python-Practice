s="XIV"
value=0
numerals=['I','V','X','L','C','D','M']
values=[1,5,10,50,100,500,1000]
num_conversion=[]
temp=[]
total_value=0
neg_val=0
#goal="MMXXIMIXDMIVIXIDIMI"
for i in s:
    temp.append(i)

for i in temp:
    location=numerals.index(i)
    num_conversion.append(values[location])
num_conversion.append(0)
#print(num_conversion)
for i in num_conversion:
    location=num_conversion.index(i)
    if i == 1 and num_conversion[location+1] >1:
        neg_val=neg_val+2                               #neg_value goes up by double due to adding EVERY number together
    if i == 10 and num_conversion[location +1] >10:
        neg_val=neg_val+20
    if i == 100 and num_conversion[location +1] >100:
        neg_val=neg_val+200
    total_value=total_value+int(i)                      #This adds EVERY number together, fixed with neg_value*2
    num_conversion[num_conversion.index(i)]="X"         #This replaces i(1000) (ex.'M'CMXCIV) with "X" to handle duplicates
total_value=total_value-neg_val
print(total_value)