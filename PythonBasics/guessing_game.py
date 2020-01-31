# Guessing Game
from random import randint


# Rules of the game
print('You have to guess the Magic Number!')
print('Magic number is an integer between 1 and 100')
print('You will get warmer when your guess is closer to the Magic Number')
print('You will get colder if your guess is farther away from the Magic Number')

# Generate random magic number
magic_number = randint(1,100)
num_of_guesses = 0

# Guess number first time
print('Guess the number:')
prev_guess = int(input())
num_of_guesses += 1

# Check if guess is close to magic number
if prev_guess not in range(1,101):
    print('OUT OF BOUNDS')
    print('Guess number again')
    prev_guess = int(input())

if prev_guess == magic_number:
    print('Hooray! You guessed the Magic Number!')
elif abs(prev_guess - magic_number) > 10:
    print('COLD!')
else:
    print('WARM!')

while(True):
    print('Guess the number')
    next_guess = int(input())
    num_of_guesses += 1
    if next_guess not in range(1,101):
        print('OUT OF BOUNDS')
        print('Guess number again')
        next_guess = int(input())
    
    if next_guess == magic_number:
        print(f'Hooray! You guessed the Magic Number in {num_of_guesses} guesses!')
        break;
    elif abs(prev_guess - magic_number) > abs(next_guess - magic_number):
        print('Warmer')
        prev_guess = next_guess
    else:
        print('Colder')
        prev_guess = next_guess
