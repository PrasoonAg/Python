import random

# Card Deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []
computer_card = []

# Getting random cards
for i in range(0, 2):
    player_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))


# Logic for Player's card and Computer's card i.e. [11, 11] -> 22 then converting to [1, 11]:
# Function for dealing with this
def correct(input_deck):
    while sum(input_deck) == 22 and 11 in input_deck:
        if input_deck.count(11) == 2:
            input_deck[0] = 1


if sum(player_card) == 22 and sum(computer_card) == 22:
    correct(player_card)
    correct(computer_card)

elif sum(player_card) == 22 and 11 in player_card:
    correct(player_card)

elif sum(computer_card) == 22 and 11 in computer_card:
    correct(computer_card)

print(f" Your cards: {player_card}, current score: {sum(player_card)} \n Computer's first card: {computer_card[0]}")


# Result check
def check(player_card, computer_card):
    print(
        f"Your final hand: {player_card}, final score: {sum(player_card)} \n Computer's final hand: {computer_card}, final score: {sum(computer_card)}")

    if sum(player_card) > sum(computer_card):
        if sum(player_card) > 21:
            print("Player went over. Player lose")
        else:
            print("Player wins")

    elif sum(player_card) < sum(computer_card):
        if sum(computer_card) > 21:
            print("Computer went over. Player win!")
        else:
            print("Computer wins")

    else:
        print("Draw")


# Logic for getting cards i.e. player deck
if sum(player_card) == 21:
    check(player_card, computer_card)
else:
    while sum(player_card) <= 21:

        choose = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        # Hit (Add card to player deck)
        if choose == 'y':

            player_card.append(random.choice(cards))

            while sum(player_card) > 21 and 11 in player_card:
                player_card[player_card.index(11)] = 1
                break

            if sum(player_card) > 21:
                print(
                    f" Your cards: {player_card}, current score: {sum(player_card)} \n Computer's first card: {computer_card[0]}")
                check(player_card, computer_card)
                break
            print(
                f" Your cards: {player_card}, current score: {sum(player_card)} \n Computer's first card: {computer_card[0]}")

        # Logic for Computer's final deck
        elif choose == 'n':

            while sum(computer_card) < 17:
                computer_card.append(random.choice(cards))
                if sum(computer_card) > 21 and 11 in computer_card:
                    computer_card[computer_card.index(11)] = 1
                    continue
            print(f"Added card: {computer_card} -> {sum(computer_card)}")

            if 17 <= sum(computer_card) <= 21:
                check(player_card, computer_card)
                break

            check(player_card, computer_card)

            break
        else:
            print("Error! Choose correct input")