# Sets are like unordered list, but all elements in sets are unique.

nums = {1,2,3,4,5}
print(nums)
print(type(nums))
# Note that sets has curly braces, just like dictionary. But sets do not have key-value pair. You can consider sets as dictionary with only keys, since keys are unique.

# To add an element in set
nums.add(6)
print(nums)
nums.add(5)
print(nums)
# Notice that 5 is not added to nums because 5 was already present in nums set.

# To initialize an empty set
nums = set()
# Sets are mostly used to get unique elements from a list.
num_list = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,5,6,6,7]
nums = set(num_list) # Initialize nums set using num_list
print(nums)
