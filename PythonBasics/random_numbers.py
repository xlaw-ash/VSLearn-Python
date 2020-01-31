from random import randint
from random import shuffle

# Python can generate random numbers
# In some cases, random results are required.

# The most common case is a coin toss. Write code to display result of coin tossed 10 times.
coin_toss = {
    1 : 'Head',
    2 : 'Tail'
}
for test in range(1, 11): # Run loop from 1 to 10
    print(f'Test {test}: {coin_toss[randint(1,2)]}') # randint is used to generate random number between 1 and 2. In randint, both start and end are included.

# Rolling a die is another example. Write code to display result of two dies tossed simultaneously 10 times.
print('Roll\tDie-1\tDie-2\tTotal')
print('----\t-----\t-----\t-----')
for roll in range(1, 11):
    die1 = randint(1,6)
    die2 = randint(1,6)
    print(f'{roll}\t{die1}\t{die2}\t{die1 + die2}')

# Use shuffle to shuffle a list. Example: Shuffle tracks of an album.
tracks = list(range(1,11)) # Create a list of tracks from 1 to 10
print(tracks)
shuffle(tracks) # Use shuffle to shuffle the list. Note that in-place modification of list takes place.
print(tracks)
