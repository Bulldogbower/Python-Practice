import sys
#sys.setrecursionlimit(40)

##Below are a few test cases
#s="()"                #True
#s="(}{)"              #False
#s="({{{{}}}))"        #False
#s="(([]){})"          #True
#s="[](){}}{"          #False
#s="[({(())}[()])]"    #True
#s="[({(())}[()])]"    #True
s="[]{}()[]()[]{}()[()()]"


openings=['(','[','{']
closings=[')',']','}']
string=[]
reference=[]
for i in s:
    reference.append(i)
print("Ref " + str(reference))
# for i in s:
#     string.append(i)
# string.append(9)
location=0

def NoMorePairs():
    print(False)
    sys.exit()

def DeletePairs(string, reference):
    #global string
    #global location
    #global reference
    # print("Within DeletePairs")
    # print("String: "+ str(string))
    # print("Reference: "+str(reference))
    if "Y" not in string:
        NoMorePairs()
    if string.__contains__("Y"):
        location=string.index("Y")
        #print(location)
        del reference[location]
        del reference[location]
        del string[location]
        del string[location]
    #print(len(reference))
    if string.__contains__("Y"):
        DeletePairs(string, reference)
    print("Reference after deletion: "+str(reference))
    if len(reference)>0:
        FindInnerPair()
    if len(reference)==0:
        print(True)
        sys.exit()



def FindInnerPair():
    print("Within FindInnerPair")
    global string
    #global location
    print("Reference within FindInnerPair: " + str(reference))
    string=list(reference)
    string.append(9)
    print(string)
    for i in string:
        #print(i)
        if i!=9:
            next_char=string[string.index(i)+1]
            #print("i= "+str(i), " at location "+str(string.index(i)) + ", next character is " + str(next_char), " at location "+ str(string.index(i)+1))
        #if i=="(" or i=="[" or i=="{":
            #print("Found an open "+str(i))
        #if i==")" or i=="]" or i=="}":
            #print("Found a close "+str(i))
        if i=="(" and next_char==")" or i=="[" and next_char=="]" or i=="{" and next_char=="}":
            #print("Pair Found, turning them into Y's")
            string[string.index(i)]= "Y"
            string[string.index(next_char)]= "Y1"
            #print(string) 
        elif i!="Y" and i!="Y1" and i!=9:
            location=string.index(i)
            #print("Turning non pairs into _'s")
            string[location]="_"
    print(string)
    print(reference)
    DeletePairs(string, reference)

if len(s)%2!=0:
    print(False)
else:
    FindInnerPair()

