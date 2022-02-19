#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = []
#num = input("Give me a number: ")
#for numbers in a:
#    if numbers <= int(num):
#      b.append(numbers)
#
#print(b)
        #print(elements)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#number=(input("Give me a number "))
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for element in a:
#    if element in b:
#        c.append(element)
#print(c)

#if int(number) in a:
#    print("Number in list a")
#if int(number) in b:
#   print("Number in list b")
#if int(number) in c:
#    print("Number in list c")
#else:
#    print("Number not in any list")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#word = input("Give me a word ")
#reverse = word[::-1]
#print(word)
#print(reverse)
#if word == reverse:
#    print("Word is a palindrome")
#else:
#    print("Word is not a palindrome")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#b = []
#c = []
#for element in a:
#    if element %2:
#        c.append(element)
#    else:
#        b.append(element)
#print(b)
#print(c)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Rock Paper Scissors
#Ask user for input
#Randomize computer choice
#Compare user and computer
#Display winner


#import random
#def start():
#    print("")
#
#while True:
#    print("Welcome to my game")
#    Choices=["rock","paper","scissors"]
#    user_input=input("rock, paper, or scissors? ")
#    #print(user_input)
#    computer_choice=random.choice(Choices)
#    print("Computer picks "+computer_choice)
#    if user_input == computer_choice:
#        print("There was a tie!")
#    if user_input == "rock" and computer_choice == "scissors" or user_input == "paper" and computer_choice == "rock" or user_input == "scissors" and computer_choice == "paper":
#        print("You Win!")
#    if user_input == "rock" and computer_choice == "paper" or user_input == "paper" and computer_choice == "scissors" or user_input == "scissors" and computer_choice == "rock":
#        print("You lose!")
#    play_again=input("Do you want to play again? (Y/N) ")
#    if play_again=="Y" or "y":
#        start()
#    if play_again=="N" or "n":
#        end()

#Fibonacci sequence
#ask for number i.e. 1
#display fibonacci from that number i.e. 1,1,2,3,5,8

#a=[]
#length=int(input("How many digits do you want in your Fibonacci sequence? "))
#user_num=int(input("Give me a number "))
#a.append(user_num)
#a.append(user_num + user_num)
#for item in a:
#    add=a[-1] + a[-2]
#    a.append(add)
#    if len(a) == length:
#        break
#print(a)

#Remove duplicate names/numbers from set [set()]
#names = (2, 4, 6, 5, 5, 2, 4, 6)
#names_sorted = []
#for i in names:
#    if i not in names_sorted:
#        names_sorted.append(i)
#print(names_sorted)

##################Random password generator
# strength=input("Press ENTER for a random password")
# import random
# char=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",'r','s','t','u','v','w','x','y','z')
# cap_char=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
# num=("0","1","2","3","4","5","6","7","8","9")
# spec_char=("!","@","#","$","%","^","&","*")
# final_pass=list()
# temp_pass=()
# for element in char:
#    #print(random.choice(char))
#    final_pass.append(random.choice(char))
#    #print(final_pass)
#    #if len(final_pass)>=4:
#    #    break
#    final_pass.append(random.choice(cap_char))
#    #if len(final_pass) >= 8:
#    #    break
#    final_pass.append(random.choice(num))
#    #if len(final_pass) >= 12:
#    #    break
#    final_pass.append(random.choice(spec_char))
#    if len(final_pass) >= 16:
#        break
#random.shuffle(final_pass)
#printable_pass="".join(final_pass)
#print(printable_pass)


##########bulls and cows
#Ask a user for a 4 digit number
#Randomize separate 4 digit number
#If user number has similar digits, tell user how many
#Let user guess again on same number

# import random
# def start():
#     print("")
#     numbers=('0','1','2','3','4','5','6','7','8','9')
#     num=[]
#     user_num_split=[]
#     for elements in numbers:
#         num.append(random.choice(numbers))
#         if len(num) == 4:
#             break
#
#
# #    print("random number (for testing)" + str(num))
#     print("Welcome to my Cows and Bulls game! Try to guess the number I'm thinking of. If you guess the correct number in the correct spot ")
#     print("you'll get 1 Cow. If you guess an incorrect number, or the correct number in the wrong spot, you'll get a Bull. Good luck!")
#     print("(Press CTRL + C to quit at any time)")
#
#     while True:
#         bulls = 0
#         cows = 0
#         user_num_split = []
#         user_num = input("Give me a 4 digit number ")
#         if len(user_num) !=4:
#             print("Must be 4 digits")
#             start()
#         for element in user_num:
#             user_num_split.append(element)
#         #print("User_num_split " + str(user_num_split))
#         if user_num_split[0] == num[0]:
#             cows=(int(cows)+1)
#         else:
#             bulls=(int(bulls)+1)
#         if user_num_split[1] == num[1]:
#             cows=(int(cows)+1)
#         else:
#             bulls=(int(bulls)+1)
#         if user_num_split[2] == num[2]:
#             cows=(int(cows)+1)
#         else:
#             bulls=(int(bulls)+1)
#         if user_num_split[3] == num[3]:
#             cows=(int(cows)+1)
#         else:
#             bulls=(int(bulls)+1)
#         print(str(bulls) + str("Cow(s)!"))
#         print(str(cows) + str("Bull(s)!"))
#         if cows==4:
#             print("You win! The number was ",str(num))
#             play_again = input("Would you like to play again?(Y/N)")
#             if play_again=="Y" or play_again=="y":
#                 start()
#             else:
#                 break
# start()

############################################################################
#Have a user input a number and see if it's in the sorted list
# list=[*range(0,99)] #[*range(0,99)] This creates a list with a range from 0-99 BUT does not include 99
# num=int(input("Give me a 2 digit number "))
# if num in list:
#     print("Number is in list")
#############################################################################
#Write contents to a file
#with open('test.txt', 'w') as open_file: #'w' means write, 'r' means read only, 'r+' means rw
#    open_file.write('This is a test')
#############################################################################
#Read a list of names, count how many of each name, delete duplicates, print unique names
# names = []
# names_final = []
# a=[]
# a_count=0
# b=[]
# b_count=0
# c=[]
# c_count=0
#
# def NameSorter():
#     with open('names.txt') as names_file:
#         for name in names_file:
#             if name not in names:
#                 #names.append(name)
#                 names.append(name.rstrip('\n')) #name.rstrip('\n') gets rid of the '\n' that python makes with new lines
#             for name in names:
#                 if name not in names_final:
#                     names_final.append(name)
#         print("These are the names in the document:", ', '.join(names_final))
# def NameCounter():
#     a_count = 0
#     b_count = 0
#     c_count = 0
#     a.append(names_final[0])
#     for i in names:
#         if i in a:
#             a_count=(a_count+1)
#     print(', '.join(a),"appears", a_count, "times") #', '.join(a) prints "['Darth']" as "Darth"
#     b.append(names_final[1])
#     for i in names:
#         if i in b:
#             b_count=(b_count+1)
#     print(', '.join(b),"appears", b_count, "times")
#     c.append(names_final[2])
#     for i in names:
#         if i in c:
#             c_count=(c_count+1)
#     print(', '.join(c),"appears", c_count, "times")
#
#
# NameSorter()
# NameCounter()
############################################################################
##User thinks of a number
#Computer asks questions to guess number, if wrong user inputs "Lower" or "Higher"
#I think it'd be optimal if it guesses 50 first, then 25 or 75 accordingly.
# num=50
# print("Think of a number and I will try to guess it. If I get it wrong, let me know if the answer is 'higher' or 'lower'")
# answer1=input("Is the number "+str(num)+"? (If no, please put 'higher' or 'lower') ")
# if answer1=='lower':
#     num=num/2
#     answer2=input("Is the number "+str(num)+"? ")
# if answer1=='higher':
#     num=num+25
#     answer2=input("Is the number "+str(num)+"? ")
#
#
# if answer2=='lower':
#     answer3=input("Is the number 12? ")
# if answer3=='lower':
#     answer3=input("Is the number 6? ")
# if answer3=='higher':
#     answer4=input("Is the number 18? ")
################################################################
def SearchFile():
    user_start_date =input('What date would you like to start your query from? (Format: MM/DD/YY)')
    user_end_date =input('What date would you like to end your query at? (Format: MM/DD/YY)')
    if len(user_start_date) != 8 or len(user_end_date) != 8:
        print("Incorrect date format")
        SearchFile()
    start_month = user_start_date[0:2]  # MM START
    start_month = start_month.zfill(2)  # Makes sure MM is 2 digits i.e '02'
    start_day = user_start_date[3:5]  # DD START
    start_year = user_start_date[6:8]  # YY START
    start_year = start_year.zfill(2)  # Makes sure YY is 2 digits i.e '02'
    end_month = user_end_date[0:2]  # MM END
    end_day = user_end_date[3:5]  # DD END
    end_year = user_end_date[6:8]  # YY END
    days = range((int(start_day)), (int(end_day)+1))
    list_of_days = []
    for i in days:
        list_of_days.append(i)
    #print(list_of_days)
    #for i in list_of_days:
        #no_brackets = str(list_of_days[0:99]).strip('[]')
    warn_level = input("What level of error to search for? (NOTICE, INFO, WARNING or CRIT)")
    for i in list_of_days:
        day=i
        day=str(day).zfill(2) #Makes sure DD is 2 digits i.e '02'
        #print(day)
        dates_to_look_for = start_month + '/' + str(day) + '/' + start_year
        #print(dates_to_look_for)
        log = open('log.txt')
        for line in log:
            if line.startswith(dates_to_look_for) and line.__contains__(warn_level.upper()): #.startswith(start_month+'/'+str(day)+'/'+start_year):
                print(line)
            #else:
            #    print("No logs of selected level from selected date range")
            #    SearchFile()
SearchFile()
################################################################################







