#Select 2 cards randomly
#Add them together (Use 11 for ace now, work on 2 values later)
#Ask user if they want to hit, stay, raise
import random
import sys
cards=[2,3,4,5,6,7,8,9,10,"J","Q","K"]
suites=["H","D","S","C"]
ace=["A"]
royals=["J","Q","K"]

def GetHand():
    global hand
    global hand_value
    global hand_suites
    global hand_with_suites
    hand=[]
    value=[]
    hand_suites=[]
    hand_value_of_cards=[]
    hand_value=0
    for elements in cards:
        hand.append(random.choice(cards))
        if len(hand)==2:
            break
    for elements in suites:
        hand_suites.append(random.choice(suites))
        if len(hand_suites) ==2:
            break
    hand_with_suites=str(hand[0])+str(hand_suites[0]), str(hand[1])+str(hand_suites[1])                     #Making it a usable variable for later
    print("Your cards are " + hand_with_suites[0], hand_with_suites[1])                                     #Prints as 4C,QD
    for i in hand:
        #print(i)
        if royals.__contains__(i):
            #print("Royalty found")
            #i=10
            #print(i)
            hand_value=hand_value+10
        else:
            hand_value=hand_value+i
    print(hand_value)                                                                                       #Value of both cards added together (4C + QD = 15)
GetHand()

def Hit():
    #print("Within hit")
    global hand
    global hand_value
    hit_value=0
    hit=[]
    hit_suites=[]
    for elements in cards:
        hit.append(random.choice(cards))
        if len(hit) ==1:
            break
    hand.append(hit[0])
    for elements in suites:
        hit_suites.append(random.choice(suites))
        if len(hit_suites) ==1:
            break
    hand_suites.append(hit_suites)
    print("Card is "+str(hit[0])+ str(hit_suites[0]))
    #hand_with_suites=str(hand[0])+str(hand_suites[0]), str(hand[1])+str(hand_suites[1])
    hit_with_suites=str(hit[0])+ str(hit_suites[0])
    print("Hand is "+ str(hand_with_suites[0] + " " + str(hand_with_suites[1])) + " " + str(hit_with_suites))
    for i in hit:
        if royals.__contains__(i):
            #print("Royalty found")
            hand_value=hand_value+10
        else:
            hand_value=hand_value+i
    print(hand_value)
    HitStayOrRaise()

def HitStayOrRaise():
    global hand
    global hand_value
    # print(hand)
    # print(hand_value)
    if hand_value>21:
        answer=input("Busted! Wanna play again?" )
        if answer=='yes':
            GetHand
        else:
            sys.exit("Goodbye!")
    if hand_value==21:
        print("You got 21! Let's hope the house doesn't beat you")
    if hand_value<21:
        play=input("Would you like to hit or stay? ")
        if play=="stay":
            print("You decided to stay, now the house will play")
        if play=="hit":
            Hit()            
HitStayOrRaise()

