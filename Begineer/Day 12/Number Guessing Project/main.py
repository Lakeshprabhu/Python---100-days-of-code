#Number guessing game
import random
from pickle import GLOBAL

logo = '''$$$$$$$$\ $$\   $$\ $$$$$$$$\       $$\   $$\ $$\   $$\ $$\      $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\  $$\   $$\ $$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\  $$$$$$\         $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\ 
\__$$  __|$$ |  $$ |$$  _____|      $$$\  $$ |$$ |  $$ |$$$\    $$$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |$$  __$$\       $$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|
   $$ |   $$ |  $$ |$$ |            $$$$\ $$ |$$ |  $$ |$$$$\  $$$$ |$$ |  $$ |$$ |      $$ |  $$ |      $$ /  \__|$$ |  $$ |$$ |      $$ /  \__|$$ /  \__|  $$ |  $$$$\ $$ |$$ /  \__|      $$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |      
   $$ |   $$$$$$$$ |$$$$$\          $$ $$\$$ |$$ |  $$ |$$\$$\$$ $$ |$$$$$$$\ |$$$$$\    $$$$$$$  |      $$ |$$$$\ $$ |  $$ |$$$$$\    \$$$$$$\  \$$$$$$\    $$ |  $$ $$\$$ |$$ |$$$$\       $$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\    
   $$ |   $$  __$$ |$$  __|         $$ \$$$$ |$$ |  $$ |$$ \$$$  $$ |$$  __$$\ $$  __|   $$  __$$<       $$ |\_$$ |$$ |  $$ |$$  __|    \____$$\  \____$$\   $$ |  $$ \$$$$ |$$ |\_$$ |      $$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|   
   $$ |   $$ |  $$ |$$ |            $$ |\$$$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$\   $$ |$$\   $$ |  $$ |  $$ |\$$$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |      
   $$ |   $$ |  $$ |$$$$$$$$\       $$ | \$$ |\$$$$$$  |$$ | \_/ $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |      \$$$$$$  |\$$$$$$  |$$$$$$$$\ \$$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |\$$$$$$  |      \$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\ 
   \__|   \__|  \__|\________|      \__|  \__| \______/ \__|     \__|\_______/ \________|\__|  \__|       \______/  \______/ \________| \______/  \______/ \______|\__|  \__| \______/        \______/ \__|  \__|\__|     \__|\________|
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        '''



List_of_Numbers = []
for i in range(1,101):
    List_of_Numbers.append(i)


chosen_number = random.choice(List_of_Numbers)





def play():
    global chosen_number
    print(logo)
    print("Welcome to the number guessing game \n Im thinking of a number between 1 to 100.")
    difficulty= (input("Type 'easy' or 'hard':")).lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5


    while attempts !=0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess=int(input("Make a guess:"))
        if guess != chosen_number:
            if guess < chosen_number:
                print("Too low \nGuess again")
                attempts-=1
            elif guess > chosen_number:
                print("Too high \nGuess again")
                attempts-=1
        if guess == chosen_number:
            print(f"You got it ! The answer was {guess} ")
            return

    print("You run  out of guesses , You loose")


play()