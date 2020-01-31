# Tuples can be considered as immutable list. i.e. Elements of tuoles can't be modified.
# Tuples have parenthesis, instead of square brackets.

my_tuple = (1,2,3)
print(my_tuple)
print(my_tuple[1])

# my_tuple[2] = 4 # This statement will cause assignment error because element in tuple can't be modified.
my_tuple = (1,3,5,1,3,2,5,7,1,3)
print(my_tuple.count(1)) # Prints number of 1s in the tuple
print(my_tuple.index(5)) # Prints the first index of 5 in the tuple
print(my_tuple[4:8])

# Tuples are similar to list. The only difference is that tuples are immutable.

nums = (1,2,3,4,5)
flowers = ('lily', 'rose', 'sunflower')
mixed = nums + flowers
print(mixed)

# Note that tuples do not have append/insert/pop/remove methods. You can create your own methods for tuples.
# I want my mixed tuple to be (1,2,3,'lily','sunflower',4,5)

flowers = flowers[:1] + flowers[2:] # Removed 'rose' (element at index 1) from flowers
mixed = nums[:3] + flowers + nums[3:5] # Inserts flowers in between 3 and 4
print(mixed)

# Tuples can be nested. Remember the matrix example from list.
row1 = (1,2,3)
row2 = (4,5,6)
row3 = (7,8,9)
matrix = (row1,row2,row3)
print(matrix)
print(matrix[2][1]) # Prints 2nd element (index = 1) of 3rd row (index = 2), i.e. 8
for row in matrix:
    for item in row:
        print(item,end=' ')
    print()
