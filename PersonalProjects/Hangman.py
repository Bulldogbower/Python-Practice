import random
import sys
list = []
#word = []
temp_list=[]
wordlist = open('wordlist.txt')
letter_count=[]
correct_guesses=[]
correct_times=0
tries=6
sorted_answer=[]
location_of_correct_guess=0
#guess = input("Guess a letter ")
temp_word=[]
all_guesses=[]


def RandomWord():
    global letter_count
    global all_guesses
    global sorted_answer
    global temp_word
    letter_count.clear()
    all_guesses.clear()
    sorted_answer.clear()
    temp_word.clear()
    word=[]
    for i in wordlist:
        list.append(i.rstrip('\n').lower())                 #Strips the '\n' of new lines
    word.append(random.choice(list))
    #print(word)
    #print("Word is " + str(word[0]) + " For Debugging purposes. Delete when done testing")  # [0] gets rid of "['WORD']" when printing
    for i in word[0]:
        letter_count.append(i)
    for i in letter_count:
        temp_word.append("_")
    # print(letter_count)
    print("Word is " + str(temp_word))

    extra_sorted_answer = []
    #print(letter_count)
    #Guess()

# def OrganizeTheLetters():
#     print()

def Guess():
    HangManDesign()
    global all_guesses
    global tries
    global temp_word
    guess = input("Guess a letter ")
    sorted_answer=[]
    all_guesses.append(guess)
    print("Current guesses: " + str(all_guesses))
    for i in letter_count:
        #print(i)
        if letter_count.__contains__(guess.lower()):
            print(str(guess) +" is correct")
            if guess not in correct_guesses:
                correct_guesses.append(guess.lower())
            #print("That letter is in spot " + str(letter_count.index(guess)+1))
            for i in letter_count:
                if i in correct_guesses:
                    sorted_answer.append(i)
            for i in sorted_answer:
                temp_word[letter_count.index(i)]=i
            # temp_word.insert(letter_count.index(guess),sorted_answer)
            # print("Letter_count" + str(letter_count))
            # print("The correct guesses are " + str(correct_guesses))
            # print("The sorted guesses are " + str(sorted_answer))
            if len(sorted_answer) > len(correct_guesses) and sorted_answer != temp_word:
                #print("Duplicates exist")
                #Where are "l"s in balloon
                dup_location=letter_count.index(guess,letter_count.index(guess)+1)
                temp_word[dup_location]=guess
                correct_guesses.append(guess)
            print("Word is " + str(temp_word))
            print("Tries left: "+ str(tries))
            if sorted_answer == letter_count:
                print("Success")
                EndGame()
            Guess()
        else:
            print("That is incorrect")
            print("Word is " + str(temp_word))
            tries-=1
            if tries == 0:
                print("Game Over")
                HangManDesign()
                EndGame()
            print("Tries left: "+ str(tries))
            Guess()

def EndGame():
    play_again=input("Would you like to play again?(yes/no)")
    if play_again=="yes":
        global letter_count
        global all_guesses
        global sorted_answer
        global temp_word
        global correct_guesses
        correct_guesses.clear()
        letter_count.clear()
        all_guesses.clear()
        sorted_answer.clear()
        temp_word.clear()
        global tries
        tries=6
        return RandomWord()
    if play_again=="no":
        sys.exit("Goodbye!")
    else:
        print("please type 'yes' or 'no'")
        EndGame()

def HangManDesign():
    if tries==6:
        print("""
               +---+
               |   |
                   |
                   |
                   |
                   |
            =========""")
        return
    if tries==5:
        print("""
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =========""")
    if tries==4:
        print("""
               +---+
               |   |
               O   |
               |   |
                   |
                   |
             =========""")
    if tries==3:
        print("""
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
             =========""")
    if tries==2:
        print("""
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
             =========""")
    if tries == 1:
        print("""
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
             =========""")
    if tries == 0:
        print("""
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
             =========
             *Sad Noises*""")
        print("Word was " + str(letter_count))



RandomWord()
Guess()
