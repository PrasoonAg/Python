import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
attempts = 0
game_over = True

computer_number = random.randint(1,100)

def logic(attempts_left):
    
    while attempts_left != 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))
        
        if guess == computer_number:
            print("You guessed was correct")
            game_over = False
            return game_over
        elif guess > computer_number:
            print("Too High")
            attempts_left -= 1
        else:
            print("Too low")
            attempts_left -= 1
        if guess != computer_number:
            print("Guess again.")
        
    if attempts_left == 0:
        print("you lose!!")
        game_over = False
        return game_over

while game_over == True :
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if mode == 'easy':
        attempts = 10
    elif mode == 'hard':
        attempts = 5
    else:
        print("Enter a valid string.")
    if mode == 'easy' or mode == 'hard':
        logic(attempts)