# It takes input of the name of the city you grew up in and a pet name, gives result a combine name for a band.
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of thier city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
  
print("Welecome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
print(city)
pet_name = input("What's your pet's name?\n")
print(pet_name)
print(f"Your band name could be {city} {pet_name}\n")