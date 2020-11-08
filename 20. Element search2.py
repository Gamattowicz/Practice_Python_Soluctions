import random


def element_search(list, num):
    list.sort()
    while len(list) != 1:
        if len(list) == 0:
            return False
        else:
            m = len(list)//2
            mid = list[m]

            if num == mid:
                return True
            elif num > mid:
                list = list[m+1:]
            else:
                list = list[:m]
    return False


if __name__ == '__main__':
    list = [random.randint(0, 100) for i in range(50)]
    print(sorted(list))
    num = int(input('Enter a number: '))
    print(element_search(list, num))
