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

#Write your code below this line 👇

types = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Papper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("Invalid number. You lose!")
else:
  print(types[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose: ")
  print(types[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose, sucker!")
  elif computer_choice > user_choice:
    print("You lose, sucker!")
  elif user_choice > computer_choice:
    print("You win, sucker!")
  elif computer_choice == user_choice:
    print("It's a draw, sucker!")
        

