''' Python 3.9
22.10.2020

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right. (Hint: remember
to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when
the game ends, print this out.'''

import random

number = random.randint(1, 9)

count = 0
user = 0

while user != number and user != 'exit':
    user = int(input('Guess a number: '))

    if user == 'exit':
        print('Game over')
        break

    count += 1

    if user < number:
        print('Too low')

    elif user > number:
        print('Too high')

    else:
        print("You're right!")


print("You guessed in {} try!".format(count))
