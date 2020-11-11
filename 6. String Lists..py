''' Python 3.9
21.10.2020

Ask the user for a string and print out whether this string is a palindrome or
not. A palindrome is a string that reads the same forwards and backwards.)'''


def reverse(word):
    drow = ' '
    for i in range(len(word)):
        drow += word[len(word) - 1 - i]

    return drow


word = input('Choose your word: ')

word = word.lower()

drow = reverse(word)
if word != drow:
    print("It's palindrome")
else:
    print("It's not palindrome")


print('*'*50)

word = input('Choose your word: ')

word = word.lower()

drow = word[::-1]

if word != drow:
    print("It's palindrome")
else:
    print("It's not palindrome")
