import random,art

cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_deck = []
comp_deck = []

def play():
    user_sum = 0
    comp_sum = 0
    round1 = 2
    first_comp = random.choice(cards)
    comp_deck.append(first_comp)

    while user_sum < 21:
        for i in range(round1):
            user_choice = random.choice(cards)
            user_sum+=user_choice
            user_deck.append(user_choice)
        round1 = 1
        print(f"Your cards:{print(user_deck)}, current score: {user_sum}")
        print(f"Computer's first card: {first_comp}")

        if user_sum > 21:
            break


        swap_turn=input("Type 'y' to get another card , type 'n' to pass :")
        if swap_turn == "y":
            pass
        if swap_turn == "n":
            break


    while comp_sum <=17 and user_sum <22:
        comp_choice = random.choice(cards)
        comp_sum+=comp_choice
        comp_deck.append(comp_choice)

    print(f"Your final hand: {print(user_deck)} , final score: {user_sum}")
    print(f"Computer's final hand:{print(comp_deck)} , final score: {comp_sum}")

    if user_sum == comp_sum:
        print("Its a draw")

    if user_sum == 21:
        print("You win")

    elif comp_sum == 21:
        print("You loose")


    if user_sum > 21:
        print("You went over. You loose")

    elif user_sum == comp_sum:
        print("Its a draw")

    elif (21 - user_sum) < (21 - comp_sum):
        print("You win , You beat the game")

    elif (21 - user_sum) > (21 - comp_sum):
        print("You loose ")

    return 0







def game_start():
    while  True:
        print(art.logo)
        start= (input("Do you want to play a game og blackjack ? \
(Type 'y' for yes and 'n' for no): ")).lower()
        if start == "y":
            pass
        if start =="n":
            break

        play()


game_start()