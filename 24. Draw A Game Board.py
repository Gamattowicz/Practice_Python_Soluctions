height = int(input('Enter height: '))
width = int(input('Enter width: '))


def top_cell(num):
    a = ' ---'*num
    return a


def side_cell(num):
    b = '|   '*num
    return b


def board(height, width):
    for i in range(height):
        print(top_cell(width))
        print(side_cell(width+1))
    print(top_cell(width))


board(height, width)
