nums = [1,2,3,4,5]
print(nums)
flowers = ['rose','jasmine','lotus','lily','sunflower']
print(flowers)
mixed = [1,2,'rose',4.57,'lily']
print(mixed)
# Note that unlike other languages, Python list can have different types of elements. mixed list has int, string, and float type variables.

# Unlike strings, lists are mutable. Which means, elements in list can be modified.
mixed[1] = 'sunflower'
mixed[2] = 3
mixed[4] = 'jasmine'
print(mixed)

# List concatenation.
concat = nums + flowers
print(concat)

mixed.append('rose') # Adds an element at the end of list
print(mixed)
mixed.insert(0, 'lily') # Inserts element at the specified index.
mixed.insert(4, 2.18)
print(mixed)
# Note that 'lily' is inserted at 0th index and 1 is shifted from 0th index to 1st index.
# An example to understand insert
nums = [1,2,3,5,6,7] # Note that I forgot to add 4 in the list
# nums.insert(3, 4)
nums = nums[:3] + [4] + nums[3:]
print(nums) # The output is same as nums.insert(3, 4)

# To remove an element from list, we can use pop method.
print(nums.pop()) # Pop will remove the element at the end of the list.
print(nums)
# Notice that pop method returns the removed item.
popped_item = nums.pop()
print(popped_item)
print(nums)
print(nums.pop(3)) # Pop can also be used to remove item at specific index
print(nums)
# To remove a specific item by it's value instead of index, you can't use pop. You can use remove method.
print(nums.remove(5))
print(nums)
# Notice that remove does not return the removed item. So, if you want to use the removed item, you have to use pop method.

print(flowers)
# print(flowers.pop('lily')) # This statement will give you error because pop method only takes index as parameter. To remove 'lily', use remove method.
flowers.remove('lily')
print(flowers)
flowers = flowers + ['lily'] * 3 # Multiplication concatenation is similar to string
print(flowers)

flowers.remove('lily')
print(flowers)
# Notice that only first occurence of 'lily' is removed. To remove all occurences, use loops, which will come later.
flowers.remove('lily')
print(flowers)

# You can sort the list in a specific order.
flowers.sort() # By default, sort is in ascending order.
print(flowers)
# Notice that sort method did not return any list. It sorts the list in-place without returning anything.
print(type(flowers.sort())) # sort method does not return anything. That is why the type is NoneType.

nums = [10,5,8,23,17,3,6,1]
# To print the numbers in descending order, we can use sort and reverse.
nums.sort()
nums.reverse() # Just like sort, reverse method doesn't return anything.
print(nums)

# A shorter way is to sort a list in reverse order using reverse parameter
nums = [10,5,8,23,17,3,6,1]
nums.sort(reverse = True)
print(nums)
# Note that sort method is not needed to reverse the order of list.

# Lists can be nested. Which means, you can put two or more lists in one list.
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
matrix = [row1,row2,row3]
print(matrix) # Notice that in matrix list, each element represents a row.
print(matrix[1][2]) # Prints 3rd element of second row, i.e. 6.
# Remember the indexing of elements starts from 0. matrix[1] returns row2. matrix[1][2] returns row2[2], which is 3rd element of row2, which is 6.

# We can use loops to print the matrix. Loops will come later.
for row in matrix:
    for element in row:
        print(element, end=' ') # note that end parameter can be used to specify the character at end of line in print. By default, new line character (\n) is at the end of the line.
    print()

# zip two lists : creates a zip of touples in which first element of touple is from first list and second element of touple is from second list
codes = [101,102,103,104,105]
courses = ['English', 'Math', 'Physics', 'Chemistry', 'Computer']
print(list(zip(codes, courses)))

# Note that length of lists need not be same
codes = [101,102,103]
courses = ['English', 'Math', 'Physics', 'Chemistry', 'Computer']
print(list(zip(codes, courses)))

codes = [101,102,103,104,105]
courses = ['English', 'Math', 'Physics', 'Chemistry', 'Computer']
for code, course in zip(codes, courses):
    print(f'{code} : {course}')