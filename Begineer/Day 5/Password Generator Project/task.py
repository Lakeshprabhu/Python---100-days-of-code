import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#EASY

for i in range(0,nr_letters):
    chosen_letter = random.randint(0,len(letters) - 1)
    print(letters[chosen_letter],end="")

for i in range(0,nr_symbols):
    chosen_symbol = random.randint(0,len(symbols) - 1)
    print(symbols[chosen_symbol],end="")

for i in  range(0,nr_numbers):
    chosen_number = random.randint(0,len(numbers) - 1)
    print(numbers[chosen_number],end="")

print("\n   \
      \
      \
      \
HARD \n")

# HARD

for i in range(0,nr_letters+nr_numbers+nr_symbols):
    character_chooser = random.randint(1,3)
    if character_chooser == 1:
        chosen_letter = random.randint(0, len(letters) - 1)
        print(letters[chosen_letter], end="")
    elif character_chooser == 2:
        chosen_symbol = random.randint(0, len(symbols) - 1)
        print(symbols[chosen_symbol], end="")
    else:
        chosen_number = random.randint(0, len(numbers) - 1)
        print(numbers[chosen_number], end="")



#Efficient


password = ""
for i in range(0,nr_letters+nr_numbers+nr_symbols):
    
