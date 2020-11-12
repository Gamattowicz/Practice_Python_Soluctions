''' Python 3.9
22.10.2020

Write a program (using functions!) that asks the user for a long
string containing multiple words. Print back to the user the same
string, except with the words in backwards order. For example,
say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.'''


def reversal():
    word = input('Write some words for me, sir! ').split(' ')
    drow = ' '.join(word[::-1])
    return drow


print(reversal())
