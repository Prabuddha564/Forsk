#Optional Task: Rock Paper Sissors

"""
Que.
Make a game of rock, paper scissors against the computer.

Problem:
          Tell the user about the Game Instruction
          Tell user to enter either rock,paper or scissors
          Get the response from the user
          Compare user selection and computer selection
          Display who wins.

Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    Make an enumerated variable type to store choices.

Hint
  Rock  vs paper   -> paper wins
  Rock  vs scissor -> Rock wins
  paper vs scissor -> scissor wins

"""
# Soln. By - Prabuddha Bhalerao ,On - 20/07/2022

import random
from enum import IntEnum
#Lets Start the Game
print("We are about to play Rock Paper Scissors Mr. User, So")

class Choice(IntEnum):
    ''' choice options to int '''
    Rock = 0
    Paper = 1
    Scissors = 2

# Values
user_choice = input("n/Enter your choice (rock, paper or scissors): ")
valid_choice = ["rock","paper","scissor"]
computer_choice = random.choice(valid_choice)

#Show
print("Mr. User choose",user_choice,"and Computer choose",computer_choice,".")

while True:
    if user_choice == computer_choice:
        print("Both users selected",user_choice," It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print('enter valid input')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
