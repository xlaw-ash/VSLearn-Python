# for loops have some special uses with List Comprehensions

# Make a list of letters in greeting string.
greeting = 'Hello World!'
letters = []
for letter in greeting:
    letters.append(letter)
print(letters)
letters = []
# Above 3 statements can be combined in a single line.
letters = [letter for letter in greeting] # letter is added to list. It is same as append.
print(letters)
# Note that list comprehension is same as append method with loop. It is just a short way to create list.

# List comprehensions can be used with arithmetic operations
# Make a list of multiples of 5 from 1 to 50, i.e. Table of 5.
table_of_5 = [x * 5 for x in range(1,11)]
print(table_of_5)

# Make list of even numbers from 1 to 20
evens = [x for x in range(1,11) if x % 2 == 0]
print(evens)

# Nested List comprehensions
# Make a list of even multiples of 5
evens_5 = [x for x in [x * 5 for x in range(1,11)] if x % 2 == 0]
print(evens_5)
# Above nested statement looks a bit confusing, but it is quite simple. Inner list is created and then outer list is created from inner list.
# [x * 5 for x in range(1,11)] creates a list of multiples of 5 from 5 to 50.
# Outer list comprehension takes input from list of multiples of 5 and creates new list of even numbers in list of multiples of 5.
# Creating one list and then creating next list using first list is same as nested list comprehension.

# Note that above example is just to show nested list compreshension.
# More efficient way to make a list of even multiples of 5 by creating only one list.
evens_5 = []
evens_5 = [x * 5 for x in range(1,11) if (x * 5) % 2 == 0]
print(evens_5)
