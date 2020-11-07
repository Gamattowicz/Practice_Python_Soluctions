def reversal():
    word = input('Write some words for me, sir! ').split(' ')
    drow = ' '.join(word[::-1])
    return drow


print(reversal())
