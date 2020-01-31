# Booleans have only two values. Either True or False.
# Booleans are used for conditions.
yes = True
no = False
print(yes)
print(type(yes))

# Booleans are mostly used with logical operators. There are three main logical operators.
# 'and' operator between two conditions returns True only when both conditions are True, else it returns False.
print("'and' operator matrix")
print('and\tTrue\tFalse')
print(f'True\t{True and True}\t{True and False}')
print(f'False\t{False and True}\t{False and False}')

# 'or' operator between two conditions returns True when either condition is True.
print("'or' operator matrix")
print('or\tTrue\tFalse')
print(f'True\t{True or True}\t{True or False}')
print(f'False\t{False or True}\t{False or False}')

# 'not' operator is applied to a condition to reverse it's result. In other words, True becomes False and False becomes True
print(f'not false: {not False}')
print(f'not True: {not True}')

# There are various comparison operators which are used to get boolean result. [Left Value operator Right Value]
# '>' : Greater than operator. Returns True when Left Value is greater than Right Value.
print(3>2) # Prints True since 3 is greater than 2.
print(2>5) # Prints False

# '<' : Less than operator. Returns True when Left Value is less than Right Value.
print(3<2) # Prints False since 3 is greater than 2
print(2<5) # Prints True

# '==' : Equality operator. Returns True when both values are equal.
print(3==3) # Returns True since 3 is equal to 3.
print(3.0==3) # Returns True even though 3.0 is float and 3 is int because the values are same.
# Note that to check equality, two equal signs are used because single equal sign is used as assignment operator. a = 3 assigns 3 to a. a == 3 will check if a is equal to 3.

# '!=' : 'Not equal to operator'. This operator is used to check if the two values are unqual.
# Check if num is odd.
num = 15
print(num % 2 != 0) # Odd numbers are divisible by 2. So, the remainder of num divided by 2 should not be 0. This prints True.
# Check if num is even.
num = 20
print(num % 2 == 0) # Even numbers are divisible by 2. So, the remainder of num divided by 2 should be 0. This prints True

# '>=' : Returns True when Left Value is greater than or equal to Right value
# '<=' : Returns True when Left Value is less than or equal to Right value
# Print True if num is between 10 and 20 inclusive
num = 15
print(num >= 10 and num <= 20) # Prints True
num = 25
print(num >= 10 and num <= 20) # Prints False
