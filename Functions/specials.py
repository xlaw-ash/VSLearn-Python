# map function allows a function to iterate through a list and returns an iterator of updated values

def isPrime(num):
    if num == 1:
        return False
    elif(num % 2 == 0 and num > 2):
        return False
    for divisor in range(3, int(num ** (1/2)) + 1, 2):
        if(num % divisor == 0):
            return False
    return True

nums = [2,5,9,1,12,15,13,16,23,25,11]
print(list(map(isPrime,nums)))

# filter function allows a function to iterate through a list and return an iterator of elements in that list for which the function returns True
print(list(filter(isPrime, nums)))

# map and filter functions are useful to make code shorter.
# Lambda Expressions are popular way to make code shorter. Lambda Expressions are used when name of function is not required and function can be defined in one line.
# Create a list of perfect squares between 2 and 100

nums = [num for num in range(2,101)]
print(list(filter(lambda num : (num ** (1/2)).is_integer(), nums)))

# Above way is a bit confusing. But, when you read code one-by-one, it's easy to read.
# lambda creates an unnamed function which returns True if square root of a number is a whole number (perfect square)
# filter takes two arguements, unnamed function (lambda expression) and nums list
# list makes list of iterable returned by filter

# The more you learn about Python, the more you will learn to keep your code as short as possible
# Python's main idea is to keep code as short as possible
# Create a list of perfect squares between 2 and 100 in one line

print(list(filter(lambda num : (num ** (1/2)).is_integer(), [num for num in range(2,101)])))

# Special parameters for functions, *args and **kwargs
# *args is an iterable parameter. It means function can take any number of parameters
# **kwargs means function can take any number of key-value pairs as parameters

# calculate net total of items in a bill.
def net_total(*args):
    return sum(args)

item1 = 10
item2 = 15
item3 = 18
item4 = 25
item5 = 12
print(f'Net Total: {net_total(item1,item2,item3,item4,item5)}')

def net_total_with_items(**kwargs):
    total = 0
    for (name, price) in kwargs.items():
        print(f"{name}: {price}")
        total += price
    print(f'Total: {total}')

net_total_with_items(item1 = 10, item2 = 15, item3 = 18, item4 = 25, item5 = 12)
