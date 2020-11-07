import datetime

name = input('What is your name? ')
age = int(input('How old are you? '))

today = datetime.datetime.now()


age1 = ((today.year - age) + 100)

print('In {} {} will be 100 years old'.format(age1, name))
