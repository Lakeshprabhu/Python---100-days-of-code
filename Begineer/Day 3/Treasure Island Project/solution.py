print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island \n Your mission is to find the treasure")

choice_1=(input("You see a crossroads . \n \
        Choose to either travel down the left or right path: ")).lower()

if choice_1 == "left":
    choice_2 = ((input("After travelling down the left path you come across a lake,\
     Do you want to swim or wait or the current to subside: "))).lower()
    if choice_2 == "wait":
        choice_3 = (input("After waiting , you come across a boat , you then use it travel to a island . \n \
        \nThere you stand before a house with three doors. \n A red door, A blue one and finally a yellow door \
        \nWhich door do you want to enter ?: ")).lower()
        if choice_3 == "yellow":
            print("You Win")
        elif choice_3 == "red":
            print("Burned by fire. \n Game Over")
        elif choice_3 == "blue":
            print("Eaten by Beasts. \n Game Over")






    else:
        print("Attacked by trout. \n Game Over")
else:
    print("You fell into hole \n \
          Game Over ")