import random

def play():
    computer_guess = random.choice(['r', 's', 'p'])

    player_choice = input("What is your choice? r for rock, s for scissor, or p for paper? ")

    if(player_choice == computer_guess):
        return f'tie computer guessed {computer_guess} you guessed {player_choice}'

    if isWinPlayer(computer_guess, player_choice):
        return f'Congratulations! You won! computer guessed {computer_guess} you guessed {player_choice}'

    return f'You lost computer guessed {computer_guess} you guessed {player_choice}'
        

def isWinPlayer(computer, player):
    if(computer == 's' and player == 'r') or (computer == 'p' and player == 's') or (computer == 'r' and player == 'p'):
        return True

def play_again():
    playagain = input("Would you like to play again? y or n? ")
    if (playagain == 'y'):
        return True
    if (playagain == 'n'):
        return

print(play())

playagain = 'y'

while playagain is 'y':
    if play_again():
        print(play())
    else: 
        break

