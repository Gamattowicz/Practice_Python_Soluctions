''' Python 3.9
22.10.2020

Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the user
to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next
number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

num = int(input('How many Fibonnaci numbers do you wanna generate? '))


def fibonacci(num):
    fib = []
    for i in range(1, num+1):
        if i == 1:
            fib.append(1)
        elif i == 2:
            fib.append(1)
        else:
            fib.append(fib[i-2]+fib[i-3])

    return fib


print(fibonacci(num))
