
number = int(input('Input number to check: '))
check = int(input('Input number to divide by: '))


if number % 4 == 0:
    print("{} is a multiple of 4".format(number))
elif number % 2 == 0:
    print('{} is an even number'.format(number))
else:
    print("{} is an odd number".format(number))


if number % check == 0:
    print('{} divides evenly by {}'.format(number, check))
else:
    print('{} does not divide evenly by {}'.format(number, check))
