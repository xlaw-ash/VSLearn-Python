import math

# Functions are important in programming.
# Functions are created when a code segment needs to be used in multiple places.
# Functions make code easier to read and understand.
# Functions are used to perform a specific task to make code look cleaner.

# Print all prime numbers between 1 and 100. A prime number is a number which is only divisble by 1 and itself.
# For example, 23 is a prime number. 10 is not a prime number because it is divisible by 2 and 5 too.
# 1 is not a prime number.

for num in range(2,101): # Run loop from 2 to 100
    isPrime = True # Assume that number is Prime
    if(num % 2 == 0 and num > 2): # Checks all even divisors
        isPrime = False
    for divisor in range(3, int(math.sqrt(num)) + 1, 2): # Check odd divisors from 3 to square root of num.
        if(num % divisor == 0): # If num is divisible by divisor, i.e. remainder is 0, number is not prime.
            isPrime = False # Set isPrime to false and break the loop
            break
    if isPrime: # Print the number if isPrime is true
        print(num, end=' ')
print()

# Above code segment prints checks if a number is prime and prints it.
# To print prime numbers between 500 and 600, a way is to copy paste the entire code segment.
for num in range(500,600):
    isPrime = True
    if(num % 2 == 0 and num > 2):
        isPrime = False
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % divisor == 0):
            isPrime = False
            break
    if isPrime:
        print(num, end=' ')
print()

# Above way is too confusing and redundant. The logic to check if a number is prime is repeated.
# This redundancy makes code look bigger and difficult to read.
# The logic to check if a number is prime can be implemented in a function. That function can be called any number of times in program.

# To create a function, def is used. def tells Python that isPrime is a function. num is a parameter passed in function.
def isPrime(num):
    if(num % 2 == 0 and num > 2):
        return False
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % divisor == 0):
            return False # return statement ends the functions and returns a value. In this case, False is returned if divisor is divisible by num.
    return True # return True when no factor of num is found.

print([num for num in range(2,101) if isPrime(num)])
print([num for num in range(500,600) if isPrime(num)])
print([num for num in range(1000,1050) if isPrime(num)])

# Function to check if a number is prime number made program to print prime numbers within given range simple and look good.
# isPrime function can be called anywhere in this program to check if a number is prime.

# It is recommended to give a function a sensible name to understand what it does.
# For example, print is a function and it prints on console.
# Sometimes, function name is not enough to understand what a function does. docstring is used to describe a function.

def greet(name):
    '''
    Takes a single parameter
    Returns a string 'Hello name'
    '''
    return f'Hello {name}'
name = 'Mark'
print(greet(name))
help(greet) # help function takes the name of function as parameter and prints the docstring of that function. It is nice way to learn about a function.
help(print)

# A calculator which prints the result
def calculator(op, num1, num2):
    '''
    Calculator takes three parameters
    op: operator (add, sub, mul, div)
    num1: first number
    num2: second number
    Returns a string for arithmetic operation of two numbers according to op
    '''
    if op == 'add':
         print(f'{num1} + {num2} = {num1 + num2}')
    elif op == 'sub':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif op == 'mul':
        print(f'{num1} * {num2} = {num1 * num2}')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')

calculator('add', 5, 10)
calculator('sub', 5, 10)
calculator('mul', 5, 10)
calculator('div', 5, 10)

# Note that calculator function does not return any value. Functions need not return any value.
# Functions need not have parameters either.
def print_hello():
    '''
    Prints 'Hello World!' string
    '''
    print('Hello World!')

print_hello()
print(type(print_hello()))
