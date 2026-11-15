# Hangman Game
# Hangman is a classic word-guessing game where one player tries to figure out a hidden word by suggesting letters one at a time

import random

# lives = 6
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# HANGMANPICS = HANGMANPICS.reverse()
n = 0
print(HANGMANPICS[0])


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    # camel
    guess = input("Guess a letter of the word: ").lower()
    # c
    
    display = ""
    
    for letter in chosen_word: 
        if letter == guess: 
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        # lives -= 1
        n += 1
        if n == 6:
            game_over = True
            print("You Lose")
            print(HANGMANPICS[n])
            break

    print(HANGMANPICS[n])
    
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")