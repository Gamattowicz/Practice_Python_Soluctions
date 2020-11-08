table = [i for i in range(101)]


while len(table) != 0:
    m = len(table)//2
    mid = table[m]
    answer = input('{} is your number? [low/high/right] '.format(mid))
    if answer == 'right':
        print('git')
        break
    elif answer == 'high':
        table = table[m:]
    elif answer == 'low':
        table = table[:m+1]
    else:
        print('Wrong answer')
