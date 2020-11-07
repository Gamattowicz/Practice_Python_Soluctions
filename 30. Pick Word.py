import random

name = 'sowpods.txt'


def pick_word(name):
    with open(name, 'r') as f:
        print(random.choice(list(f)))


pick_word(name)
