''' Python 3.9
22.10.2020

Ask the user for a number and determine whether the number
is prime or not. (For those who have forgotten, a prime
number is a number that has no divisors.). You can
(and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.'''


num = int(input('Choose number: '))
divisors = [i for i in range(1, num+1) if num % i == 0]


def Primal_number(num):
    if num > 1:
        if len(divisors) > 2:
            print("It's not primal number! ")
        else:
            print("It's primal number! ")
        print(divisors)


Primal_number(num)
