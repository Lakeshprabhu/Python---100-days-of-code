# import the data for the celebrities
# randomly choose two celebritries , each assigned to a variable
# if correct the chosen celebrity is compared against in the next game
# goes on till the player gets wrong

import game_data,art,random


print(random.choice(game_data.data))
#TOD0 - Pass  celebrities and their followers as arguments
score = 0
def celeb_chosen():
    """Will retrieve  a random celebrity """
    celeb_traits = random.choice(game_data.data)
    return celeb_traits['name'],celeb_traits['follower_count'],celeb_traits['description'],celeb_traits['country']


def user_choice():
    """Ask's for the user choice"""
    return input("Who has more followers? Type 'A' or 'B':")



def game_over():
    """Will show the game over screen if the user guesses wrong"""
    print(f"Sorry, that's wrong. Final score: {score}")
def celeb_comparison(celebrity_1_name, celebrity_1_follower_count, celebrity_1_description, celebrity_1_country,celebrity_2_name, celebrity_2_follower_count, celebrity_2_description, celebrity_2_country):
    global score

    if celebrity_1_name == celebrity_2_name:
        while celebrity_1_name == celebrity_2_name:
            celebrity_2_name, celebrity_2_follower_count, celebrity_2_description, celebrity_2_country = celeb_chosen()

    print(f"Compare A: {celebrity_1_name}, a {celebrity_1_description}, from {celebrity_1_country}.  "+"\n"*3+f"{art.vs}")
    print(f"Compare B: {celebrity_2_name}, a {celebrity_2_description}, from {celebrity_2_country}.  ")
    user_guess=(user_choice()).upper()
    max_followers = ""
    if celebrity_1_follower_count > celebrity_2_follower_count:
        max_followers = "A"
    else:
        max_followers = "B"

    if user_guess == max_followers:
        score+=1
        print(f"You're right! Current score : {score}")

        celebrity_1_name, celebrity_1_follower_count, celebrity_1_description, celebrity_1_country = celeb_chosen()

        celeb_comparison(celebrity_2_name, celebrity_2_follower_count, celebrity_2_description, celebrity_2_country,celebrity_1_name, celebrity_1_follower_count, celebrity_1_description, celebrity_1_country)

    else:
        game_over()





#TODO - Define the logic of how the game will retrive and compare
def game_start():
    print(art.logo)
    celebrity_1_name, celebrity_1_follower_count, celebrity_1_description, celebrity_1_country = celeb_chosen()
    celebrity_2_name, celebrity_2_follower_count, celebrity_2_description, celebrity_2_country = celeb_chosen()
    celeb_comparison(celebrity_1_name, celebrity_1_follower_count, celebrity_1_description, celebrity_1_country,celebrity_2_name, celebrity_2_follower_count, celebrity_2_description, celebrity_2_country)


game_start()