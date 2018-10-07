import random
from os import system

s6 = "#############\n\
#           #\n\
#           0\n\
#         0X X0\n\
#           0\n\
#          000\n\
#         0 0 0\n\
#        0  0  0\n\
#          0 0\n\
#         0   0\n\
#        0     0\n\
#       0       0\n\
#\n\
#\n\
#"

s5 = "#############\n\
#           #\n\
#           0\n\
#         0   0\n\
#           0\n\
#          000\n\
#         0 0 0\n\
#        0  0  0\n\
#          0\n\
#         0\n\
#        0\n\
#       0\n\
#\n\
#\n\
#"

s4 = "#############\n\
#           #\n\
#           0\n\
#         0   0\n\
#           0\n\
#          000\n\
#         0 0 0\n\
#        0  0  0\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#"

s3 = "#############\n\
#           #\n\
#           0\n\
#         0   0\n\
#           0\n\
#          00\n\
#         0 0\n\
#        0  0\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#"

s2 = "#############\n\
#           #\n\
#           0\n\
#         0   0\n\
#           0\n\
#           0\n\
#           0\n\
#           0\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#"

s1 = "#############\n\
#           #\n\
#           0\n\
#         0   0\n\
#           0\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#"

s0 = "#############\n\
#           #\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#\n\
#"
hangman = []
hangman.extend((s0, s1, s2, s3, s4, s5, s6))

valid_guess = False
inc_guesses = 0            # keep track of incorrect guesses
tot_guesses = 0
letters_guessed = set()    # keep track of letters already used
guess = ''

def rand_word():
    with open('words_alpha_5.txt') as word_file:
        valid_words = list(word_file.read().split())
        randword = valid_words[random.randint(1, 360331)]
    return randword


word = rand_word()
letset = set(word)
wordlen = len(word)
wordarr = ['_'] * wordlen

print("Welcome to Hangman!")

while (inc_guesses < 6):

    while (valid_guess == False):
        guess = input("guess a letter: ")
        guess = guess.lower()
        if (guess.isalpha() and len(guess) == 1 and guess not in letters_guessed):
            valid_guess = True
            letters_guessed.add(guess)
        else:
            print("Not a valid guess. Try again\n")
    valid_guess = False
    tot_guesses += 1


    system('clear')

    if guess in letset:
        for i in range(wordlen):
            if word[i] == guess:
                wordarr[i] = guess

        if '_' not in wordarr:
            print(hangman[inc_guesses])
            print("CONGRATULATIONS, YOU HAVE WON!")
            print("The word was", word)
            print("It only took you",tot_guesses,"guesses")
            break

        print("")
        print(hangman[inc_guesses])
        print("GREAT GUESS!", end = '\n\n')
        print(' '.join(wordarr), end = '\n')

    elif guess not in letset:
        inc_guesses += 1
        print("")
        print(hangman[inc_guesses])
        if (inc_guesses == 6):
            print("YOU HAVE DIED")
            print("The word was", word)
            break
        print("INCORRECT!",(6 - inc_guesses),"MORE GUESSES LEFT!", end = '\n\n')
        print(' '.join(wordarr), end = '\n')


    
