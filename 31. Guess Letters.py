import random

name = 'sowpods.txt'


def pick_word(name):
    with open(name, 'r') as f:
        return random.choice(list(f))

def game(word):
    word = list(word)
    guessed = ['_ ' for i in range(len(word))]
    again = []
    count = 6
    letter = input('Enter your letter: ')
    while True:
        if letter.upper() in again:
            letter = '*'
            print('You already guessed!')
        elif letter.upper() in word:
            i = word.index(letter.upper())
            guessed[i] = letter.upper()
            word[i] = ''
        else:
            print(''.join(guessed))
            if letter is not '*':
                again.append(letter.upper())
            if letter.upper() not in word and letter.upper() not in guessed:
                count -= 1
                print('You left {} incorrect guess'.format(count))
                if count <1:
                    print('You won')
                    choose = input('Do you wanna play again? ')
                    if choose.upper() == 'NO':
                        break
                    elif choose.upper() == 'YES':
                        game(pick_word(name))
            letter = input('Enter your letter: ')

        if '_ ' not in guessed:
            print('You won')
            choose = input('Do you wanna play again? ')
            if choose.upper() == 'NO':
                break
            elif choose.upper() == 'YES':
                game(pick_word(name))

game(pick_word(name))