import random
from art import logo
from art import vs
from game_data import data

# TODO:
# print logo
# start game:
#   print info about person A (choose random)
#   print VS
#   print info about person B (choose random)
#   ask user who has more followers
# if user guesses right
#   print you are right and the score
#   print info about prev guessed person (make person B an A)
#   print VS
#   print info person B (choose random)
#   ask user who has more followers
# if bad guess
#   print sorry that's wrong and final score

def choose_winner(account_a, account_b):
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    if followers_a > followers_b:
        correct_answer = 'a'
        correct_account = account_a
    else:
        correct_answer = 'b'
        correct_account = account_b

    return {"answer": correct_answer, "account": correct_account}

def print_accounts_info(account_a, account_b):

    name_a = account_a["name"]
    desc_a = account_a["description"]
    country_a = account_a["country"]

    name_b = account_b["name"]
    desc_b = account_b["description"]
    country_b = account_b["country"]

    print(f"Compare A: {name_a}, a {desc_a}, from {country_a}.")
    print(vs)
    print(f"Against B: {name_b}, a {desc_b}, from {country_b}.")


def play_game():
    score = 0
    is_game_over = False
    winner = ""
    print(logo)

    while not is_game_over:
        account_a = random.choice(data)
        account_b = random.choice(data)

        if winner != "":
            account_a = winner["account"]

        winner = choose_winner(account_a, account_b)

        print_accounts_info(account_a, account_b)
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_answer == winner["answer"]:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()