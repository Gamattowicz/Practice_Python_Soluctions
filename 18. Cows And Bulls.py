import random

print('Welcome to the Cows and Bulls Game! ')


def test(num, target):
    cowbull = [0, 0]
    for i in range(len(target)):
        if target[i] == num[i]:
            cowbull[0] += 1
        else:
            if num[i] in target:
                cowbull[1] += 1
    return cowbull


def main():
    game = True
    target = str(random.choice(range(1000, 9999)))
    guess = 0

    while game:
        num = input('Enter a number: ')
        if num == 'exit':
            break
        cowbullcount = test(num, target)
        guess += 1

        print('{} cows, {} bulls'.format(cowbullcount[0], cowbullcount[1]))

        if cowbullcount[0] == 4:
            game = False
            print('You won in {} try'.format(guess))
            break
        else:
            print('Try again')


main()
