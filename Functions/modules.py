import math
import functions


# Modules in Python contains a list of related functions.
# In Python, import can import a module. For example, math is a module.
# Importing math module allows Python program to use various functions and variables in it.

print(math.sqrt(81)) # sqrt returns square root of a number
print(math.pi) # prints value of variable pi in math module
print(math.sin(math.radians(30))) # Returns sine value of x. x must be in radians. radians() converts degrees to radians

# Python files of same project can also be imported.
print(functions.isPrime(23))
# Note the output of functions is printed when you import functions.
# Python runs the imported modules when import runs.
# Make sure not to import unused modules.

import os

print(os.getcwd())
# import can be used anywhere in program. But, it is recommended to import at the top of program to avoid any confusion.
