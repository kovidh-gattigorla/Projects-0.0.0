# For the welcome to print for the Player
print('Welcome to the QUIZ :) \n')
# For the input to the Player 
Score = 0                                   # Here I am using Score for the Score i GAve it a 0
PLAY = input('Do you want to play the game ? :')
# if Yes it will take to the game i used != for not equla to and .lower() for the any kind of answer Yes or YES of yes because python is a k sensitive language
if PLAY.lower() != 'yes':
    exit()                                  # To exit from the if condition

# This lanes are still under the if condition
Name = input('What is Your name : ')
print('Lets Go',Name)   # Here i am taking the a as the variable to store the input of the user, for the Question 

a = input('What is 2+3 : ')
if a == '5':                                # If input is 5 so ('here i got a problem that is 5 can be taken as string so i used '5')
    print ('correcct :)')                 # If it is correct it will print correct
    Score += 1                            # Here Score +=1 meains Score = Score + 1
else :                                      # Else it will print the below command
    print('Incorrect ?')

# Here i take again a(as the work of 'a' variable will end for the else condition used before) if not i can also take the variable
a = int(input('What is 5+2 : '))            # i used int for the input to be integer as the answer will be takin as the integer
if a == 7 :                                 # If the a == 7 here 7 will be taken as int
    print('Correct :)')                   # It will print Correct
    Score += 1                              # If the Answer is correct It Will Show Score 1
else :                                      # If not Incorrect bellow print statment will printed
    print('Incorrect ?')

a = input('What is fullform of ML : ')   #using the a variable for the input
if a.lower()!= 'Machine Learning':       # if This the answer by the user 
    print('Correct :) ')
    Score += 1                           # Score adds one more point
else :                                   # If not it will be printing this
    print('In correct')
    
print(Name,' Score Is : ',Score)

# Again using a variable for the next question 


