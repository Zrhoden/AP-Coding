# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

claswork_submitted = input("Did you submit your classwork?")
homework_submitted = input("Did you submit your homework?")

classwork_done = claswork_submitted == 'yes'
homework_done = homework_submitted == 'yes'

if classwork_done and homework_done:
    print("You have submitted both the classwork and homework!")
elif classwork_done:
    print("You have only submitted the classwork.")
elif homework_done:
    print("You have only submitted the homework.")
else:
    print("You have not submitted the classwork or the homework.")

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.
txt = "Hello World"[::-1]
print(txt)

# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

