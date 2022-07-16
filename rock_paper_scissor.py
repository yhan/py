import random

while True:
    computer_choice = random.choice(['scissors', 'paper', 'rock'])
    user_choice = input('Do you want - rock, scissors or paper?\n')

    if computer_choice.startswith(user_choice):
        print('TIE')
    elif (user_choice == 'r' and computer_choice == 'scissors')\
            or (user_choice == 's' and computer_choice == 'paper')\
            or (user_choice == 'p' and computer_choice == 'rock'):
        print(f'comp = {computer_choice}. you win ')
    else:
        print(f'comp = {computer_choice}. you loose')
