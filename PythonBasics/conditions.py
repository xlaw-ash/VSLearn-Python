# Implement conditions when code segment needs to be executed when certain conditions meet.
# There are three statements in Python to implement conditions. if, else, and elif

# if statement
if(True):
    print('Hello World!')

if(False):
    print('This will not print')
# if statement takes condition as input. If condition is True, the code segment within if statement will exectue.
# False condition will skip the code segment within if statement.
# In above example, print statement is the code segment. When condition is True, print statement executes. When condition is False, print statement is not executed.
# The colon at the end of if statement denotes the start point of if statement. 
# All indented statements below if statement (statements with certain whitespaces at the beginning) are part of code segment within if statement.

# if statements are used with boolean conditions.
num = 9
if(num % 2 == 0):
    print(f'{num} is an even number')
# num % 2 == 0 is a condition to check if the number is even. Since remainder of any even number when divided by 2 is 0, this condition will be True for all even numbers.
# Check above statement with odd numbers.

# else statement comes after if statement. In cases when different code segments needs to be executed according to the condition, else is used.
# In above example, when number is even, print statement will be exectued to display that number is even.
# But, when number is odd, no statement is executed. There are two ways.
if(num % 2 == 0):
    print(f'{num} is an even number')
if(num % 2 != 0):
    print(f'{num} is an odd number')
# Above way is confusing. Use else statement to make it simple.
if(num % 2 == 0):
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

# Use elif statements when different code segments needs to be excuted according to more than one conditions. elif statements are used between if and else statements.
ball = 'blue'
if ball == 'white': # if checks if ball is white.
    print('Ball is white') # Execute when ball is white
elif ball == 'blue': # If ball is not white, elif will check if ball is blue
    print('Ball is blue') # Execute when ball is blue
elif(ball == 'green'): # If ball is not blue, next elif checks if ball is green
    print('Ball is green') # Execute when ball is green
else: # else statement executes at last
    print('Ball is red') # Execute when ball is neither white, nor blue, nor green.

# Note: Paranthesis for conditions are optional. Paranthesis makes it easier to read conditions, especially when multiple conditions are joined.
# Note: elif and else statements cannot exist without if statements. elif must be between if and else statements.
# Note: else is not required for elif, but it is not recommended. Use multiple if statements if else is not needed.
ball = 'blue'
if ball == 'white': # if checks if ball is white.
    print('Ball is white') # Execute when ball is white
if ball == 'blue': # if checks if ball is blue.
    print('Ball is blue') # Execute when ball is blue
if ball == 'green': # If ball is not blue, next elif checks if ball is green
    print('Ball is green') # Execute when ball is green
if ball == 'red': # else statement executes at last
    print('Ball is red') # Execute when ball is neither white, nor blue, nor green.

# In above case, the output of multiple if statements is same as using if-elif-else statements. But both are very different.

# In if-elif-else scenario, when a condition is met, all the conditions below that condition are skipped.
# If ball is white, Python prints 'Ball is white' and all belows conditional statements are skipped. 
# If ball is not white, Python will go to next elif statement to check if ball is blue. Python will skip all below statements if ball is blue.
# If ball is not blue, Python will go to next elif statement to check if ball is green. Python will skip below else statement if ball is green.
# If ball is not green, else is executed.

# In multiple if scenario, all if conditions will be checked unnecessarily. Which means Python will do unecessary work and increase execution time.
# Nested if-else
num = 25
if num % 2 == 0:
    if num % 5 == 0:
        print(f'{num} is even and multiple of 5')
    else:
        print(f'{num} is even')
else:
    if num % 5 == 0:
        print(f'{num} is odd and multiple of 5')
    else:
        print(f'{num} is odd')

# Check if year is leap year. A year is leap year if year is divisble by 4.
# Year is not leap year if it's a century, i.e. year is divisible by 100.
# But, century is a leap year if it's divisible by 400.
year = 2020
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# Use if-else conditions with strings
greeting = 'HelloHello World!'
if('Hello' in greeting): # in operator checks if 'Hello' is in the string greeting
    print('Hello')
else:
    print('Bye')

# Use if-else conditions with lists
fruits = ['apple', 'mango', 'peach']
if 'apple' in fruits:
    print('List contains apple') # Prints because list has 'apple' 
if 'banana' in fruits:
    print('List contains banana') # Does not print because list does not have 'banana'

# Join not with in operator
if 'banana' not in fruits:
    print('List does not contain banana')
