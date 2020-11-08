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
