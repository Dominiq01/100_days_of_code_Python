import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_results(user_cards, computer_cards):
    print(f"    Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def is_blackjack(user_cards, computer_cards):
    computer_score = sum(computer_cards)
    user_score = sum(user_cards)
    if computer_score == 21 or (computer_score == 21 and user_score == 21):
        print_results(user_cards, computer_cards)
        print("Computer wins with a Blackjack 😭")
        blackjack()
        return True
    elif user_score == 21:
        print_results(user_cards, computer_cards)
        print("Win with a Blackjack 😎")
        blackjack()
        return True
    return False

def is_game_over(user_cards, computer_cards):
    computer_score = sum(computer_cards)
    user_score = sum(user_cards)

    if computer_score == user_score:
        print_results(user_cards, computer_cards)
        print("It's a draw 😑")
        blackjack()
        return True
    elif user_score > 21:
        print_results(user_cards, computer_cards)
        print("You went over. You lose 😭")
        blackjack()
        return True
    elif computer_score > 21:
        print_results(user_cards, computer_cards)
        print("Opponent went over. You win 😁")
        blackjack()
        return True
    elif computer_score < user_score:
        print_results(user_cards, computer_cards)
        print("You win 😁")
        blackjack()
        return True
    elif computer_score > user_score:
        print_results(user_cards, computer_cards)
        print("You lose 😭")
        blackjack()
        return True
    return False

def blackjack():
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wants_to_play != 'y':
        print(wants_to_play)
        return
    print('\n' * 20)
    print(logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")
    game_over = is_blackjack(user_cards, computer_cards)

    while not game_over:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == 'y':
            next_card = user_cards.append(random.choice(cards))
            if next_card == 11 and sum(user_cards) > 21:
                user_cards[-1] = 1
            game_over = is_game_over(user_cards, computer_cards)
        else:
            computer_score = sum(computer_cards)
            while computer_score <= 16:
                computer_cards.append(random.choice(cards))
                computer_score = sum(computer_cards)
            game_over = is_game_over(user_cards, computer_cards)


blackjack()