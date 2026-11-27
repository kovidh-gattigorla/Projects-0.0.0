# For the random integer we need random module
import random

# Making the random integer between 1 to 100
number = random.randint(1,100)

# printing some text for the user to understand
print('**********************************Welcome to the number guessing game**********************************')
print('Guess a number between 1 to 100')

# While loop for staying in the game  
while True:
    guess = int(input('Enter the Guess number :'))                           # For taking the input from the user  

    if guess < number :                                                      # If condition for the low guess
        print('It is To Low, Try some thing Higher')
    elif guess > number :                                                    # elif for high guess
        print('It is To High, Try some thing lower')
    else :                                                                   # Elif break and give some thing Like you won 
        print('***** You Won *****')
        break