import random

# Store the ASCII art as strings, not in the print function
rock = """Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """Scissor
    _______
    ---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# The list containing the choices
game = [rock, paper, scissor]

# Get computer's choice (randomly selects between 0, 1, and 2)
comp_choice = random.randint(0, 2)

# Get user's choice
user_choice = int(input('''
Enter the value accordingly:
0. Rock
1. Paper
2. Scissor: '''))

# Check if the user's choice is valid
if user_choice < 0 or user_choice > 2:
    print("Idiot, it is a wrong choice. You lost the game!")
else:
    # Display computer's and user's choices
    print(f'The computer has chosen:\n{game[comp_choice]}')
    print(f'You have chosen:\n{game[user_choice]}')

    # Determine the winner
    if user_choice == comp_choice:
        print('Oops, it\'s a draw...')
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print('You won the game!')
    else:
        print('You lost the game!')
