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
rock_paper_scissors = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
print("Your choice: \n")
print(rock_paper_scissors[user_choice])

computer_choice = random.randint(0, 2)
print("Computer's choice: \n")
print(rock_paper_scissors[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif ((user_choice == 0 and computer_choice == 1) or
      (user_choice == 1 and computer_choice == 2) or
      (user_choice == 2 and computer_choice == 0)):
    print("You lose")
elif ((user_choice == 0 and computer_choice == 2) or
      (user_choice == 1 and computer_choice == 0) or
      (user_choice == 2 and computer_choice == 1)):
    print("You win")


