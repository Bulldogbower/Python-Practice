import random
def start():
    print("")
    numbers=('0','1','2','3','4','5','6','7','8','9')
    num=[]
    user_num_split=[]
    for elements in numbers:
        num.append(random.choice(numbers))
        if len(num) == 4:
            break


    print("random number (for testing, comment out before release)" + str(num))
    print("Welcome to my Cows and Bulls game! Try to guess the number I'm thinking of. If you guess the correct number in the correct spot ")
    print("you'll get 1 Bull. If you guess an incorrect number, or the correct number in the wrong spot, you'll get a Cow. Good luck!")
    print("(Press CTRL + C to quit at any time)")

    while True:
        cows = 0
        bulls = 0
        user_num_split = []
        user_num = input("Give me a 4 digit number ")
        for element in user_num:
            user_num_split.append(element)
        #print("User_num_split " + str(user_num_split))
        if user_num_split[0] == num[0]:
            bulls=(int(bulls)+1)
        else:
            cows=(int(cows)+1)
        if user_num_split[1] == num[1]:
            bulls=(int(bulls)+1)
        else:
            cows=(int(cows)+1)
        if user_num_split[2] == num[2]:
            bulls=(int(bulls)+1)
        else:
            cows=(int(cows)+1)
        if user_num_split[3] == num[3]:
            bulls=(int(bulls)+1)
        else:
            cows=(int(cows)+1)
        print(str(cows) + str("Cow(s)!"))
        print(str(bulls) + str("Bull(s)!"))
        if bulls==4:
            print("You win! The number was ",str(num))
            play_again = input("Would you like to play again?(Y/N)")
            if play_again=="Y" or play_again=="y":
                start()
            else:
                break
start()