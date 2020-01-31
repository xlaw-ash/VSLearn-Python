# Use loops when iterate thorough a list.
fruits = ['apple', 'mango', 'peach', 'orange', 'banana']
for fruit in fruits:
    print(fruit, end=' ')

print()
# Use loops when iterate through a dictionary.
courses = {
    101: 'English',
    102: 'Physics',
    103: 'Chemistry',
    104: 'Math',
    105: 'Computer Science'
}
# Iterate using keys.
for code in courses.keys():
    print(f'Course code of {courses[code]} is {code}')
print()
for code in courses:
    print(f'Course code of {courses[code]} is {code}')
print()
# Note that both courses and courses.keys() returns keys.
# Iterate through values without using keys
for course in courses.values():
    print(course, end=' ')
print()
# Iterate using items, i.e. key-value pair.
print(courses.items()) # items method returns key-value pair in a list.
for code, course in courses.items():
    print(f'Course code of {course} is {code}')

# Use loops to iterate through a range of numbers
for num in range(1,10):
    if(num % 2 == 0):
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
# range method takes start, end, and step parameters. start is included, while end is excluded. Step means jump.
# Iterate through 2 to 20 with a jump of 2 will print all even numbers between 2 and 20 (excluding 20).
for num in range(2,20,2):
    print(num, end=' ')
print()

# Iteration through tuples is just like lists.
# Example of unpacking a touple.
print('Matrix')
matrix = ((1,2,3),(4,5,6),(7,8,9))
for (item1,item2,item3) in matrix:
    print(f'{item1} {item2} {item3}')
# In above example, (item1, item2, item3) is a triplet touple.
# for loop iterates though each triplet touple of matrix and stores values in (item1, item2, item3) triplet touple.
# Note: In above example, a triplet touple is used because all elements in matrix were in for of a triplet touple.
# matrix = ((1,2,3),(4,5,6),(7,8))
# for (item1,item2,item3) in matrix:
#     print(f'{item1} {item2} {item3}')
# Uncomment above three lines and check the unpacking error. The error occured because third touple in matrix has two elements instead of three.
# There are not enough elements to unpack to create a triplet touple.

# while loops are similar to for loops. while loops execute according to boolean condition.
# while(True):
#     print('Infinite Loop')
# Above two line code segment is infinite while loop. Uncomment above two lines loop to run infinite loop.
# When the condition within while statement is False, the while loop ends execution.
# Print numbers from 1 to 10.
num = 1
while(num <= 10):
    print(num, end=' ')
    num = num + 1
print(f'\nnum = {num}')
# while loop executes print statement till num was less than and equal to 10. When num became 11, while loop ended.
# Use else to print that while loop ended execution
num = 1
while(num <= 10):
    print(num, end=' ')
    num = num + 1
else:
    print(f'\nLoop ends because num = {num} is greater than 10')

# break and continue statements
# break is used to end the loop when a condition is met.
# continue is used to jump to the start of loop when a condition is met.

# Example: Implement a calculator.
print('Calculator')
print('----------')
while(True): # Use True condition in while to run calculator indefinitely till user closes the calculator
    print('1 - Add')
    print('2 - Subtract')
    print('3 - Mulitply')
    print('4 - Divide')
    print('5 - Exit')
    print('Enter your choice:')
    choice = int(input())
    if choice >= 1 and choice <= 4: # Check if choice is between 1 and 4
        print('Enter first number: ')
        num1 = int(input())
        print('Enter second number: ')
        num2 = int(input())
        if choice == 1: # Add
            print(f'{num1} + {num2} = {num1 + num2}')
        elif choice == 2: # Subtract
            print(f'{num1} - {num2} = {num1 - num2}')
        elif choice == 3: # Multiply
            print(f'{num1} * {num2} = {num1 * num2}')
        else: # Divide
            print(f'{num1} / {num2} = {num1 / num2}')
    elif choice == 5: # Exit
        print('Thank you for using calculator!')
        break # ends the loop to close the calculator
    else: # Choice is other than 1, 2, 3, 4, and 5
        print('Incorrect choice')
        continue # Jumps to the begin of calculator app
# Note that continue in above case is optional.
