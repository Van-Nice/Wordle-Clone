import random

words_path = "assets/word-files/five-letter-words.txt"

with open(words_path, 'r') as words_file:
    words = [line.strip() for line in words_file]

random_word = random.choice(words)

def guess1():
    guess = input("Enter a 5 letter word:\n")
    if len(guess) > 5 or len(guess) < 5 or guess.isalpha() == False:
        print("Invalid input, must be 5 characters and alphabetic")
        guess1()
    return guess

# create game loop
run = True
while run:
    print("Welcome to wordle v2!\nThe rules are the same as wordle you get 6 tries to guess a 5 letter word!\n")
    guess1()
    run = False


