import random

# Game choices:
choices = ["rock", "paper", "scissor"]

# ASCII art
gesture = [
    ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        '''
,
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

# My choice
index_mine = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor:\n")
if index_mine == "0" or index_mine == "1" or index_mine == "2":
    index_mine = int(index_mine)
    print(gesture[index_mine])


    # Computer choice
    computer = random.choice(gesture)
    index_computer = gesture.index(computer)
    print("Computer choose: ", computer)


    # Game logic
    if index_mine == index_computer:
        print("Draw")
    elif index_mine == 0 and index_computer == 2:
        print("You win!")
    elif index_mine == 1 and index_computer == 0:
        print("You win!")
    elif index_mine == 2 and index_computer == 1:
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Enter a valid input.")