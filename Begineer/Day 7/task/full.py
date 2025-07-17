from typing import final

import hangman_words
import random

import hangman_art


# Todo 1: choose a word from the word list and the set of lives

chosen_word = random.choice(hangman_words.word_list)

lives = len(chosen_word)

user_guess = []

final_word = ""
level = 6
#Todo 2: Create a looping hangman game

print(hangman_art.logo)
game_start = True


print(chosen_word)
chosen_letters = []
for i in chosen_word:
    if i not in chosen_letters:
        chosen_letters.append(i)

#Todo 3: Create a word generator

print("word to guess: ",end="")
for i in range(len(chosen_word)):
    print("_",end="")
print()

while game_start:
    print(chosen_letters)

    print(f"\n********************{lives}/{len(chosen_word)} LIVES LEFT********************")
    #Todo 4 : Receive a user input
    user_choice = input("Guess a letter:")
    print("Word to guess: ",end="")
    count = 0

    for i in range(len(chosen_word)):

        if chosen_word[i] in user_guess:
            print(chosen_word[i],end="")



        elif user_choice == chosen_word[i] :
            print(user_choice,end="")

            user_guess.append(user_choice)

        elif user_choice != chosen_word[i]:
            print("_",end="")





    if user_choice not in chosen_word:
        lives-=1
        if level != 1:
            level-=1
        if lives == 0:
            level-=1

    print(hangman_art.stages[level])





    for ch in chosen_letters:
       if ch not in user_guess:

           final_word= False


       if ch == chosen_letters[-1] and ch in user_guess:
           print("\nYou guessed the word")
           game_start = False











    if lives == 0:
        print(f"You couldn't guess the word : - {chosen_word} \nGAME OVER")

        game_start = False
