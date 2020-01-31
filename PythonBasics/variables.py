# Assign 25 to a
a = 25
print(type(a))

# Assign 25.70 to a
a = 25.70
print(type(a))

# Assign 'Hello' tot a
a = 'Hello'
print(type(a))

# Notice that type of variable a changes every time a different type of value is assigned to a.
# In Python, variable have dynamic typing. Programming languages like C++, Java have static typing.

# Assign 25 to a and 75 to b. Add a and b and assign that value to sum.
a = 25
b = 75
sum = a + b
print(sum)

a = 'hello'
# Uncomment below line.
# print(a + b) 

# Notice the error. This error occured because string type variable cannot be added to int type variable.
# String type variable can only be concatenated with String type variable
b = '5'
print(a + b)

# Since '5' is a string type variable because of single quotes, now a and b can be concatenated.
# Another way to concatenate string type variable with int type variable
b = 5
print(a + str(b)) # str(b) converted b to str. Which means int type 5 was converted to string type '5'.

# Uncomment below line
# print(b + a)
# Notice the error. This error occured because you tried to add a string to number, which is invalid in arithmetic.

a = 25
b = '75'
# Uncomment below line
# print(a + b)
# Notice that you got same error because '75' is a string type variable.
print(a + int(b)) # b is converted to int type. Which means '75' is converted to 75

# Note that Python can detect numbers as string type. Only numbers can be converted from string to number.
# 'Hello' cannot be converted to number. An error will occur if you try int('hello')
# print(int('hello'))
