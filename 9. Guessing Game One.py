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
