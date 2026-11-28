# For the random integer we need random module
import random

range = input('Enter a random Number :')

# Making the random integer by the user

if range.isdigit():                                    # using this if condition for the user to give the number of gussing range
    range = int(range)
    if range <= 0:                                     # If range is lower then 0 or 0
        print('Enter some big number then 0')
else :                                                 # else for the first if condition if it is not a digit is false
    print('enter a nummber')
    exit()                                             # for the exit from condition

# printing some text for the user to understand
print('********************************************Welcome to the number guessing game********************************************')
print('Guess a number between 0 to ',range)

range = random.randint(0,range)                        # to make the range from 0 to the user input

# While loop for staying in the game  
while True:
    guess = int(input('Enter the Guess number :'))                           # For taking the input from the user  

    if guess < range :                                                      # If condition for the low guess
        print('It is To Low, Try some thing Higher')
    elif guess > range :                                                    # elif for high guess
        print('It is To High, Try some thing lower')
    else :                                                                   # Elif break and give some thing Like you won 
        print('***** You Won *****')
        break