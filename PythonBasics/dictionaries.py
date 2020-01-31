# Note: Dictionary in Python is not like Oxford Dictionary. Dictionary is a data structure with key-value pair.
# Dictionaries are unorderd lists of key-value pair. Keys must be unique. Dictionaries can't be sorted because there is no order.
# Dictionaries are partial mutable. This means that the keys in dictionary can't be modified, but the values can be modified.

# An example is subject-marks pair in exam marksheet.
marksheet = {'English': 89,'Math': 92,'Computer': 93}
print(marksheet)
# Above way is short, but not easy to read. There is another way to write.
marksheet = {
    'English': 89,
    'Math': 92,
    'Computer': 93,
}
print(marksheet)
print(marksheet['English']) # Prints the marks of English

# Oh no! I forgot to add science in the dictionary. Don't worry, it's easy to add another key.
marksheet['Science'] = 98
print(marksheet)

# I made a mistake. I got 88 marks in English. Values can be modified, so don't worry.
marksheet['English'] = 88
print(marksheet)

# Lists can have any type of keys and values, but keys must be unique and same type of keys is recommended. Nested dictionaries are allowed.
# An example is Mark's profile

mark_profile = {
    'name' : 'Mark',
    'age' : 20,
    'hobbies': ['music', 'dance', 'games'],
    'marksheet': marksheet
}
print(mark_profile)
print(mark_profile['age']) # Prints Mark's age
print(mark_profile['hobbies'][2]) # Prints Mark's hobbies at index = 2, which is games.
print(mark_profile['marksheet']['Science']) # Prints Mark's marks in Science

# print(mark_profile[0]) # This line gives error because dictionaries store values as key-value pair, not in an order. Since 0 is not a key in mark_profile, it gives KeyError: 0
# Another way to get a value from dictionary is to use get method.
print(mark_profile.get('age')) # Prints age of Mark

# Note that there is a difference between using square brackets and get methods.
# print(mark_profile.get(0)) # 0 is not a key in mark_profile. Using square barackets gives KeyError: 0, while get method returns None.

# Note: It is very important to remember that keys are unique in dictionary.
# Remember below example, because this is very important!
marksheet = {
    'English': 88,
    'Math': 92,
    'Computer': 93,
    'Science': 98,
    'Math': 98
}
# Note that by mistake I added 'Math' twice. [These mistakes can be common in big projects when you make dictionaries using various methods]
print(marksheet)
# Check the output carefully. Value of 'Math' key is 98, not 92.
# Python will not show an error when you add key which already exists in the dictionary. It will update the existing key's value.
