# Guess The Number Game

"""
Que.
     The computer will think of a random number from 1 to 10 as 
    secret number.
     Then ask you ( Player ) to guess the number and store as 
    guess number.

     Compare the guess number with the secret number.
    
     If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
     If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

# Solution by Prabudha Bhalerao on 18/07/2022

# To make computer think of random number 1 to 10
import random

secret_number = random.randint(1,10)

# to ask player to input gussed number

guess_number = int(input("Guess The Number between 1 to 10 :"))


#Result Part, If Player guess right number, he wins :
    
if (guess_number == secret_number):
    print("Player Wins and Computer lose")
# If player gusses wrong number, He Lose:    
else:
    print("Player Lose and Computer Wins")
        







