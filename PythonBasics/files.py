import os # os package is imported to use it's methods.


# Reading and Writing files is very important in programming.
# To open a file for read or write, there is open method in Python.

my_file = open('hello.txt', mode='w')
my_file.write('Hello World!')
my_file.close()

# Notice that 'hello.txt' file is created in current directory. Hello World! is displayed in first line of file.
# Two parameters are provided in open method. First parameter is path of file, second parameter is mode.
# 'hello.txt' means that file is opened in current directory. Current directory is the directory in which the program is running.
# Note that current directory is NOT the directory in which program is saved, it is the directory in which you are currently running the program.
# 'w' mode is write mode. In this mode, a file can be written. If the file doesn't exist, it creates the file.

# To read a file, open file in read mode.
my_file = open('hello.txt', mode='r')
content = my_file.read()
print(content)
my_file.close()

# Notice that I have used close method each time I opened a file. It is good practice to close a file after opening it to prevent various file issues.
# For example, a file is opened in a program and you forgot to close it. If the program is running, you cannot delete the file.
# There are many file-related issues which can be caused by forgetting to close the file.
# It is easy to forget to add close method when write hundreds of lines of code after opening a file.
# To solve that issue, you can use with in Python.

with open('hello.txt', 'r') as my_file:
    new_content = my_file.read()
print(new_content) # Variables defined within with statement can be accessed after with.
# with statement opens the file as my_file and closes it as it ends. You don't have to worry about close statement.

# Let's learn about path. In above statement, you are opening files in your current directory. To help Python locate the file, one must provide proper location of file.
# There are two kinds of paths, relative and absolute.
# Relative path starts from current directory. I am running the program in pylearn directory, so pylearn is current directory.
# hello.txt file is created in pylearn directory, even though files.py program is in basics directory.
# Relative path of hello.txt file is 'hello.txt'
# Absolute path of hello.txt is 'C:\Users\Ash\Documents\programming\pylearn\hello.txt'
# It is recommended to use relative path in programs instead of absolute path.
# For example, in Linux/MacOs, there is root directory instead of C: and absolute path is completely different. So, if use the absolute path, it will give an error.
# Another example, user Mark creates a project folder 'project' in Documents. In project folder, there are two file. program.py and input.txt. program.py reads input.txt.
# Mark gives absolute path of input.txt to read file. 'C:\Users\Mark\Documents\project\input.txt'
# Mark submits this project to his professor. His professor, Stuart, saves this project in Mark folder in his Documents.
# Stuart runs the program and gets error because input.txt exists in 'C:\Users\Stuart\Documents\Mark\project' folder. Stuart gives zero to Mark.

# In Windows, backward slashes (\) are used. Since backward slash is used for escape characters, (\\) is used to tell Python this is (\) and not an escape character.
with open('C:\\Users\\Ash\\Documents\\programming\\pylearn\\hello.txt', mode='r') as my_file:
    content_absolute = my_file.read()
    print(content_absolute)

# You can also use forward slashes. So, don't worry if that looks ugly! Linux and MacOs uses forward slashes.
with open('C:/Users/Ash/Documents/programming/pylearn/hello.txt', mode='r') as my_file:
    content_absolute = my_file.read()
    print(content_absolute)

# Note that hello.txt is in pylearn folder because I am running files.py in pylearn folder. If I run files.py in basics folder, hello.txt will be created in basics folder.
# Try to run it from some other folder, like Documents, and see the result.

# with open('/basics/new_dir/test_file1.txt', 'r') as test_file1:
#     content = test_file1.read()

# with open('/basics/new_dir/test_file1.txt', 'w') as test_file1:
#     test_file1.write('This is Test File - 1')

# Both above statements will give you error of PathNotFound instead of file not found. This is because new_dir folder does not exist in basics folder.
# Opening a file in write mode can only create a file in existing folder. It does not create a new folder. To create a new directory, you need mkdir method of os package.
# Uncomment below statement to create a new folder.
# os.mkdir('new_dir') # A new folder new_dir is created in current working directory.
# Note that if you will run this statement again after creating new_dir, it will show FileExistsError. So, comment above statement after creating new_dir.

# os package has various methods. If you want to know the current working directory from Python, you can use getcwd method.
print(os.getcwd())

# To remove a file, you can use remove method.
# with open('new_dir/test_file1.txt', mode='w') as test_file:
#     test_file.write('This is Test File 1')
# # os.remove('new_dir/test_file1.txt') # Uncomment this statement to remove test_file1.txt

# # To remove new_dir, first you have to remove all files in new_dir, then use removedirs method.
# with open('new_dir/test_file1.txt', mode='w') as test_file:
#     test_file.write('This is Test File 1')
# with open('new_dir/test_file2.txt', mode='w') as test_file:
#     test_file.write('This is Test File 2')
# with open('new_dir/test_file3.txt', mode='w') as test_file:
#     test_file.write('This is Test File 3')

# files = os.listdir('new_dir') # Returns a list of the names of all the files in the folder
# print(files)
# # Use loop to remove all files. I will use for loop.
# for file in files:
#     path = 'new_dir/' + file
#     os.remove(path)

# os.removedirs('new_dir') # Now new_dir folder can be removed
# Warning Note: Using Python methods to remove files is dangerous. You will not get any warning and the files/folders will be permanently deleted. Be very careful while using these method.

# Let's learn about various modes in which we can open file. There are three basic modes, read (r), write (w), and append (a).
# As the name suggests, read is for read only. Which means, you can only read the file. You cannot write anything in the file.
# Write mode is used to write the file. If the file does not exist, it will create a new file.
# Append mode is used to append new lines to the file. It will also create a new file if the file does not exist.
# In both write and append mode, you cannot read the files. To read a file, you need + modes.
# w+ and a+ modes are used to read the files as well. They both will create a new file if the file doesn't exist.
# There is another + mode, r+ mode. This is similar to w+ as you can read and write file, but the file will not be created if it doesn't exist.
# If you don't specify the mode in open method, it will consider read only mode (r) by default.

# Uncomment below code to see the result.
# with open('new_dir/test_file1.txt', mode='r') as test_file:
#     print(test_file.read())
# Notice the FileNotFoundError. This error occured because there is no test_file1.txt and opening in read only mode doesn't create a new file.

with open('new_dir/test_file1.txt', mode='w') as test_file:
    test_file.write('This is Test File - 1')
    test_file.write('Hello World!')

# Open test_file.txt. Notice that write method is not same as print method. Print method automatically adds new line character (\n) at the end of line. Write method doesn't.
# To create a new line, add \n explicitly.
with open('new_dir/test_file1.txt', mode='w') as test_file:
    test_file.write('This is Test File - 1\n')
    test_file.write('Hello World!\n')
    test_file.write("It's a beautiful day!")

# Hold on! When I opened test_file.txt second time, old text was overwritten by new text. You will understand what's going on soon.

with open('new_dir/test_file1.txt', mode='r') as test_file:
    print(test_file.read()) # Read method reads the whole file
    # print(test_file.read()) # Uncomment this and see what happens

# Most of the times, we need to read a file line by line
with open('new_dir/test_file1.txt', mode='r') as test_file:
    lines = test_file.readlines() # All lines of files are stored as a list in lines variable
    print(lines)
    # lines = test_file.readlines() # Uncomment these two lines and see what happens
    # print(lines)

# To really read a file line by line
with open('new_dir/test_file1.txt', mode='r') as test_file:
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())
    # print(test_file.readline()) # Uncomment this line to add one more readline method and see what happens.

# You noticed that after using read method once, you don't get anything when you use it again. If you use readlines method again, you get an empty list.
# No matter how many times you use readline method after third time, nothing will happen.
# This is happening due to cursor. A cursor is like a pointer which points at a particular place in the file.
# When you open a file in read mode, the cursor is at the beginning. When you use read and readlines commands, the cursor reads complete file and jumps to the end of file.
# When cursor is at the end of file, you do not get anythong when you use read method again.
# When readline method is used, cursor reads the line and goes to the beginning of next line. After third readline method, cursor is at end of file, so you get nothing from more readline methods.
# To read the file again, use seek method.

with open('new_dir/test_file1.txt', mode='r') as test_file:
    lines = test_file.readlines() # After reading all lines, cursor will go to end of file.
    print(lines)
    test_file.seek(0) # Cursor is set to beginning of file.
    lines = test_file.readlines() # Now readlines will return all lines again.
    print(lines)
    test_file.seek(0) # Let's test again.
    lines = test_file.readlines()
    print(lines)

# Now let's get back to the write mode. When we opened test_file.txt second time in write mode, it was overwritten by new lines.
# When you open a file in write mode, the cursor is at the beginning of the file and all the data in it overwritten.

with open('new_dir/test_file2.txt', mode='w') as test_file:
    test_file.write('This is Test File - 2\n')
    test_file.write('Hello World!')

test_file = open('new_dir/test_file2.txt', mode='w')
test_file.close()
# Notice that after running above statement, test_file2.txt is blank. Opening in write mode will be always like you are writing in a new file.
# To add new lines while keeping the old lines, open file in append mode. In append mode, the cursor is at the end of file.
with open('new_dir/test_file2.txt', mode='a') as test_file:
    test_file.write('This is Test File - 2\n')
    test_file.write('Hello World!')

with open('new_dir/test_file2.txt', mode='a') as test_file:
    test_file.write("\nIt's a beautiful day!")

# Opening file in append mode will create a file if it doesn't exist.
with open('new_dir/test_file3.txt', mode='a') as test_file:
    test_file.write("This is Test File - 3")

with open('new_dir/test_file3.txt', mode='a') as test_file:
    test_file.write('\nHello World!')
    # print(test_file.read()) # Uncomment this and notice the error. It says Not readable because the file is in append only mode. File can't be read in write only and append only modes.

with open('new_dir/test_file3.txt', mode='w+') as test_file:
    print(test_file.read())
    test_file.write('Hello World!')
    print(test_file.read())
    # Notice that nothing was printed. Now observe why. When you opened the file in write and read mode, it overwrote the file. So, it printed nothing. Cursor is at the beginning
    # Then you wrote Hello World!. Cursor is now at the end of line. So, it won't return anything again.
    test_file.seek(0)
    print(test_file.read()) # Now you will see Hello World!

with open('new_dir/test_file4.txt', mode='a') as test_file:
    test_file.write("This is Test File - 4")

with open('new_dir/test_file4.txt', mode='a+') as test_file:
    print(test_file.read()) # Cursor is at the end of file. read method won't return anything.
    test_file.write('\nHello World!') # Hello World! line is added at the end of file. Cursor jumps to end of file.
    print(test_file.read()) # Cursor is at the end of file. read method won't return anything.
    test_file.seek(0)
    print(test_file.read()) # Read method will read whole file.

with open('new_dir/test_file1.txt', mode='r') as test_file:
    print(test_file.read())
    # test_file.write('Add New Line') # Uncomment this statement. Obviously, you can't write file in read only mode. Observe that "not writable" error has occured.

# Uncomment below 5 lines (with statement) and notice the error.
# with open('new_dir/test_file5.txt', mode='r+') as test_file:
#     test_file.write('This is Test File - 5\n')
#     test_file.write('Hello World!')
#     test_file.seek(0)
#     print(test_file.read())

# FileNotFoundError occured because test_file5.txt doesn't exist.
# r+ and w+ are almost same, except w+ will create a new file if it doesn't exist, while r+ will throw an error.

test_file = open('new_dir/test_file5.txt', mode='w')
test_file.close()
# You must have noticed that when I created test_file5.txt, I didn't use with statement.
# with statement must contain a statement inside it. It can't be empty.

# with open('new_dir/test_file5.txt') as test_file: # Uncomment this statement and observe the error.
# IndentationError occured because Python uses indentation to read a block of code. with statement must contain a block of code.
# Since Python didn't find a block of code in with statement, it said that the with statement below the with statement should be inside it.

with open('new_dir/test_file5.txt', mode='r+') as test_file:
    test_file.write('This is Test File - 5\n')
    test_file.write('Hello World!')
    test_file.seek(0)
    print(test_file.read())

# It is important to understand cursors while reading and writing file.
# Each mode has it's own advantages and disadvantages. The a+ seems to be the most safest mode.
# If you will get into problems when adding new lines to the file, use seek method when you open the file.
# Better than write mode which will overwrite the file as soon as it opens.
# Warning Note: Any changes you do from program can't be undone. So, be careful when you write files.
