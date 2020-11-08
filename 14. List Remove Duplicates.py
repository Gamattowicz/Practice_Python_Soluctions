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
