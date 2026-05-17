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

print("WELCOME TO THE ROCK PAPER SCISSORS GAME")
choice = [rock, paper, scissors]
user_choice = int(input("Please enter 0 for rock, 1 for paper and 2 for scissors.\n" ))
if user_choice >= 0 and user_choice <=2:
    print(f"You chose\n {choice[user_choice]}")
else:
    print("Please provide an appropriate choice.")
    exit()

computer_choice = random.randint(0,2)
print(f"Computer chose\n {choice[computer_choice]}")

if user_choice >= 3 or user_choice <=0:
    print("You typed an invalid number!")
elif user_choice == 0 and computer_choice == 2:
    print("You Won!")
elif user_choice < computer_choice:
    print("Computer Won!")
elif user_choice < computer_choice:
    print("You Won!")
elif user_choice == user_choice:
    print("MATCH DRAW!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Won!")
