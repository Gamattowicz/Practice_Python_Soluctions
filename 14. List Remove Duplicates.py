''' Python 3.9
22.10.2020

Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that
in a different function.'''

a = [1, 2, 2, 4, 6, 7, 7, 11]


def list(a):
    b = []
    for i in a:
        if i in a and i not in b:
            b.append(i)
    return b


def sett(x):
    return list(set(x))


print(list(a))
print(sett(a))
