from game_data import data
import random
import art

print(art.logo)

# Store the selected accounts for comparison
selected_data = []

# Select a random account from the dataset
def select_random_data():
    random_index = random.randint(0, len(data) - 1)
    selected_data.append(data[random_index])


# Display selected accounts and collect their follower counts
followers = []

def display_data():
    if len(selected_data) == 0:
        select_random_data()
        select_random_data()
    else:
        followers.clear()
        select_random_data()

    for i in range(len(selected_data)):
        account = selected_data[i]
        account = list(account.values())
        followers.append(account[1])

        if i == 0:
            print(f"Compare A: {account[0]}, a {account[2]}, from {account[3]}.")
            print(art.vs)
        else:
            print(f"Against B: {account[0]}, a {account[2]}, from {account[3]}.")

    user_choice = input("Who has more followers, A or B: ").capitalize()
    return user_choice


# Compare follower counts and check the user's answer
score = 0

def check_answer(choice):
    global score

    if followers[0] > followers[1]:
        correct_answer = "A"
        del selected_data[1]
    else:
        correct_answer = "B"
        del selected_data[0]

    if choice == correct_answer:
        score += 1
        print(f"You're right! Current Score: {score}")
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return False


# Main function to control the game flow
def play():
    game_over = True

    while game_over:
        game_over = check_answer(display_data())
        print("")

play()