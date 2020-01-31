my_string = "Hello World"
print(my_string)
my_string = 'Hello World'
print(my_string)
# Both single quotes and double quotes can be used for strings

# beautiful_day = 'It's a beautiful day.
# Above string is not valid because only It is with single quotes.
# This issue can be resolved in two ways.

beautiful_day = "It's a beautiful day."
beautiful_day = 'It\'s a beautiful day.' # \ is used to add escape characters in a string.

# \', \n, \t are few escape characters

my_string = 'Hello\tWorld\nIt\'s a beautiful day' #This looks weird to read.
print(my_string)

# Another way to write
my_string = 'Hello' + '\t' + 'World' + '\n' + "It's a beautiful day" #This is string concatenation. This way is easier to read, but concatenation of string is slower.
print(my_string)

my_string = 'Hello World'
print('Length of String (' + my_string + '): ' + str(len(my_string)))

# String can also be considered as ordered list of characters. Each character has an index.
# Characters of string can be accessed using their respective indices.

# 0 1   2   3   4   5   6   7   8   9   10
# H e   l   l   o       W   o   r   l   d
print(my_string[0]) # Prints H
print(my_string[8]) # Prints r

# Get a substring -> string[first_index:last_index - 1:Jump]
print(my_string[4:]) # No last index means slice string till end
print(my_string[:7]) # No first index means slice string from beginning
print(my_string[3:10])
# Notice in above two examples that characters of index 7 and 10 are not printed.
# The range [3:10] means get character between 3 and 10, including 3 and excluding 10.

# Jump in string is used to jump characters. You can also say that print multiple of these indices.
print(my_string[::2]) # H->l->o->W->r->d (0->2->4->6->8->10)
print(my_string[::3]) # H->l->W->l (0->3->6->9)

# Negative indices can be used.
print(my_string[-1]) # Prints d
# A trick to reverse the string.
print(my_string[::-1]) # Prints characters with multiple of -1.

# String is immutable. Which means, characters of string can't be updated.
# Uncomment below statement. It will show an error because a new value can't be assigned to a character of string.
# my_string[0] = 'Z'

# Multiplication can be used to add a character multiple times.
my_string = 'z' * 10
print(my_string)

my_string = 'Hello World'
print(my_string.upper()) # Converts all characters to Upper Case
print(my_string.lower()) # Converts all characters to Lower Case
print(my_string.split()) # Creates a list of strings splitting the string by whitespace and ignoring whitespace. You can also split using characters.

# Split is very useful for reading csv (comma seperated values)
flowers = 'Rose,Lotus,Lily,Jasmine,Sunflower'
print(flowers.split(','))

# String formatting. In print statements, often variables are used.
first_name = 'Mark'
last_name = 'Scott'
age = 32
company = 'compy'

print(first_name + ' ' + last_name + ' is ' + str(age) + ' years old and works in ' + company)
# Above way of printing is difficult to understand.

# Another way of formatting is format method.
print('{} {} is {} years old and works in {}'.format(first_name, last_name, age, company))
# The parameters in format method have order. By default, string goes by order. Which means, first {} will get first parameter. second {} will get sencond parameter, and so on.

# In some cases, last name is written before first name. Mark Scott can be written as Scott Mark.
# Instead of changing the order of parameters, there is another way.
print('{1} {0} is {2} years old and works in {3}'.format(first_name, last_name, age, company))

# Using format method is still confusing because of indices.
print('{first_name} {last_name} is {age} years old and works in {company}'.format(first_name = first_name, last_name = last_name, age = age, company = company))
# Using parameters makes string easier to understand.
# Notice that the name of parameters inside format method are same as global parameters. This is acceptable in Python, but not recommended.

# A new way to format string is to use f.
print(f'{first_name} {last_name} is {age} years old and works in {company}')
# This way is much easier to understand. I recommend this way. But you need Python 3.6 and above for this.

my_string = f'{first_name} {last_name} is {age} years old and works in {company}'
print(my_string)

# Formatting float in string.
# If we have to print a bill and add taxes.
amount = 125
tax = 1.25
amount = amount + (amount * tax / 100)

print(f'Amount: {amount}')
# But Amount should not have more than two decimals.
print(f'Amount: {amount:0.2f}') # float:padding.precision
# In above example, precision is 2, so 126.5625 is rounded to 126.56

item1 = 12.76
item2 = 20.38
item3 = 65.5
item4 = 120.0
item5 = 95.81

total = item1 + item2 + item3 + item4 + item5

# To print this bill
print('Bill')
print(f'Item1: {item1}\nItem2: {item2}\nItem3: {item3}\nItem4: {item4}\nItem5: {item5}\nTotal: {total}\nNet Total: {total + (total * tax / 100)}')
# Notice that the output bill looks weird.
print('New Bill')
print(f'Item1:\t{item1:6.2f}\nItem2:\t{item2:6.2f}\nItem3:\t{item3:6.2f}\nItem4:\t{item4:6.2f}\nItem5:\t{item5:6.2f}\nTotal:\t{total:6.2f}\nTax:\t{(tax * total):6.2f}')
print(f'Net:\t{(total + (total * tax / 100)):6.2f}')
# Notice the New Bill looks more cleaner. 
# 314.45 is a float with 5 digits and one decimal. So, they take 6 spaces. 12.76 takes 5 spaces. Padding of 6 gives a additional whitespace to 12.76 to match 314.45.
# In float formatting, padding gives additional whitespace to the digits.
# For example, padding of 10 in 314.45 will give 4 additional whitespaces
print(f'{total:10.2f}') # Is same as
print(f'    {total:0.2f}')

# Notice that whitespaces are only added when padding is greater than number of spaces occupied by number.
# In other way, number of whitespaces = padding - spaces taken by number

# enumeration is used to enumerate characters of string
greeting = 'Hello World!'
for index, character in enumerate(greeting):
    print(f'{character} is at index = {index}')

# Create a list of enumeration
print(list(enumerate(greeting))) # Creates a list of characters of greeting string as (index, character) tuple
