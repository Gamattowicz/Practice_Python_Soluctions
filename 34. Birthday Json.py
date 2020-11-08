import json

with open('birthdays.json', 'r') as f:
    birth = json.load(f)


def adding():
    name = input('Who you wanna add? ')
    date = input('When {} born? '.format(name))
    birth[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birth, f)
    print('{} was added to birthday list!'.format(name))


def showing():
    print('''Welcome to the birthday dictionary program.
We know date of birthday of:''')
    for name in birth:
        print('* '+name)


def finding():
    choice = input("Who's birthday do you wanna know? ")
    if choice in birth:
        print('{} was born in {}'.format(choice, birth[choice]))
    else:
        print("We don't have date of birtday {} in our datebase".format(choice))


if __name__ == "__main__":
    while True:
        action = input('What do you wanna do? [ADD/FIND/SHOW/QUIT] ').upper()
        if action == 'SHOW':
            showing()
        elif action == 'FIND':
            finding()
        elif action == 'ADD':
            adding()
        elif action == 'QUIT':
            print('See ya!')
            break
