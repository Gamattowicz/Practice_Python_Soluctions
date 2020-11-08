''' Python 3.9
20.10.2020

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message. (Hint: order
of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button) '''

import datetime

name = input('What is your name? ')
age = int(input('How old are you? '))

today = datetime.datetime.now()


age1 = ((today.year - age) + 100)

print('In {} {} will be 100 years old'.format(age1, name))
