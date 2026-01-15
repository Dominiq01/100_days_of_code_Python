import random

from art import logo

print(logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

picked_num = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
game_over = False

if difficulty == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
else:
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5

while not game_over:
    guess = int(input("Make a guess: "))

    if guess != picked_num:
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses. Refresh the program to run again.")
            game_over = True
            break
        if guess > picked_num:
            print("Too high.")
        elif guess < picked_num:
            print("Too low.")
    else:
        print(f"You got it! The answer is {picked_num}")
        game_over = True
        break

    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")