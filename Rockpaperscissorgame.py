'''
show rules
game logic
each players has 3 options
at least 2 persons
how many times win , lose, draw
display messages


'''
#import libraries
import random 


def RPS_Game():
    # player1, player2

    # playerInput = input("Please select one of the following\nR-Rock\nP-Paper\nS-Scissors").upper()
    # computerInput = random.randint(0,2)
    # print(computerInput)
    # print(playerInput)
    print("Player1 goes first")
    player1input = input("Select one of the following\nR-Rock\nP-Paper\nS-Scissors").upper()
    player2input = input("\nSelect one of the following\nR-Rock\nP-Paper\nS-Scissors").upper()

    if player1input == player2input:
        print ("draw, play again.")
    elif player1input == 'R' and player2input == 'S':
        print("player1 wins!")
    elif player1input == 'R' and player2input == 'P':
        print ('player2 wins!')
    elif player1input == 'p' and player2input == 'S':
        print ('player2 wins!')
    elif player1input == 'p' and player2input == 'R':
        print("player2 wins!")
    elif player1input == 'S' and player2input == 'P':
        print ('player1 wins!')
    elif player1input == 'S' and player2input == 'R':
        print ('player1 wins!')
    else:
        print('Invalid input.Try again.')

   



RPS_Game()