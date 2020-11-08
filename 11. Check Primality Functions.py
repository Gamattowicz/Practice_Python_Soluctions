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
