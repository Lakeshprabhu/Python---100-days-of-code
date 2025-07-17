import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices =  [rock,paper,scissors]

comp_choice = random.randint(0,2)

user_choice =int(input("What do you choose ? Type 0 for rock , 1 for paper and 2 scissors"))

#Game Logic

if comp_choice == user_choice:
    print("Draw")

else:

    if user_choice == 0 and comp_choice == 2:
        print("You win")

    elif comp_choice > user_choice:
        print("You loose")
    elif user_choice == 2 and comp_choice == 0:
        print("You loose")
    elif user_choice > comp_choice:
        print("You win")




print("Your Choice \n " + f"{choices[user_choice]}")

print("Computer choice \n " + f"{choices[comp_choice]}")