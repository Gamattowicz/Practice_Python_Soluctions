def max_value():
    var = input('Enter your numbers: ')
    var = var.split(', ')
    var = map(int, var)
    max = 0
    for i in var:
        if i > max:
            max = i
    return max


print(max_value())
