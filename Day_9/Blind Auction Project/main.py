from art import logo
import os
print(logo)
# TODO-1: Ask the user for input
print("Welcome to the secret auction program.\n")
program_running = True
users_and_bids = {}
highest_bid = 0
winner = ""
while program_running:
    username = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    # TODO-2: Save data into dictionary {name: price}
    users_and_bids[username] = bid
    # TODO-3: Whether if new bids need to be added
    any_bidders_left = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_bidders_left != 'yes':
        program_running = False
    os.system('cls')
    print("\n" * 20)
# TODO-4: Compare bids in dictionary

highest_bid = max(users_and_bids, key=users_and_bids.get)

# for user in users_and_bids:
#
#     if users_and_bids[user] > highest_bid:
#         highest_bid = users_and_bids[user]
#         winner = user

print(f"The winner is {highest_bid} with a bid of ${users_and_bids[highest_bid]}.")

