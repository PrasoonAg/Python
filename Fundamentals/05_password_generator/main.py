import random

print("Welcome to PyPassword Generator!")

uppercase_letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

lowercase_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "-", "_", "+", "=", ".", ",", "?"
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

num_lowercase_letters = int(input("How many lowercase letters would you like in your password?\n"))
num_uppercase_letters = int(input("How many uppercase letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for i in range(0,num_lowercase_letters):
    password_list.append(random.choice(lowercase_letters))

for i in range(0,num_symbols):
    password_list.append(random.choice(symbols))

for i in range(0,num_numbers):
    password_list.append(random.choice(numbers))

for i in range(0,num_uppercase_letters):
    password_list.append(random.choice(uppercase_letters))

random.shuffle(password_list)

password = "".join(password_list)

print(f"Suggested password is: {password}")