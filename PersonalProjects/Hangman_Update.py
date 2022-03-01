import random
import sys
list = []
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


def RandomWord(letter_count, all_guesses, sorted_answer, temp_word):
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
    print("Word is " + str(temp_word))

def Guess(all_guesses, tries, temp_word):
    print("Tries left: "+ str(tries))
    HangManDesign(tries)
    guess = input("Guess a letter ")
    sorted_answer=[]
    if guess in all_guesses:
        print("Idiot, you already guessed that")
        Guess(all_guesses, tries, temp_word)
    all_guesses.append(guess)
    print("Current guesses: " + str(all_guesses))
    for i in letter_count:
        if letter_count.__contains__(guess.lower()):
            print(str(guess) +" is correct")
            if guess not in correct_guesses:
                correct_guesses.append(guess.lower())
            for i in letter_count:
                if i in correct_guesses:
                    sorted_answer.append(i)
            for i in sorted_answer:
                temp_word[letter_count.index(i)]=i
            if len(sorted_answer) > len(correct_guesses) and sorted_answer != temp_word:
                dup_location=letter_count.index(guess,letter_count.index(guess)+1)
                temp_word[dup_location]=guess
                correct_guesses.append(guess)
            print("Word is " + str(temp_word))
            #print("Tries left: "+ str(tries))
            if sorted_answer == letter_count:
                print("Success")
                tries=6
                EndGame()
            Guess(all_guesses, tries, temp_word)
        else:
            print("That is incorrect")
            print("Word is " + str(temp_word))
            tries-=1
            if tries == 0:
                print("Game Over")
                HangManDesign(tries)
                print("Word was ", letter_count)
                correct_guesses.clear()
                letter_count.clear()
                all_guesses.clear()
                sorted_answer.clear()
                temp_word.clear()
                tries=6
                EndGame()
            #print("Tries left: "+ str(tries))
            Guess(all_guesses, tries, temp_word)

def EndGame():

    play_again=input("Would you like to play again?(yes/no)")
    if play_again=="yes":
        #tries=6
        return RandomWord(letter_count, all_guesses, sorted_answer, temp_word)
    if play_again=="no":
        sys.exit("Goodbye!")
    else:
        print("please type 'yes' or 'no'")
        EndGame(tries)

def HangManDesign(tries):
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



RandomWord(letter_count, all_guesses, sorted_answer, temp_word)
Guess(all_guesses, tries, temp_word)
