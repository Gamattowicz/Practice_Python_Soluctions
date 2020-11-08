def reverse(word):
    drow = ' '
    for i in range(len(word)):
        drow += word[len(word) - 1 - i]

    return drow


word = input('Choose your word: ')

word = word.lower()

drow = reverse(word)
if word != drow:
    print("It's palindrome")
else:
    print("It's not palindrome")


print('*'*50)

word = input('Choose your word: ')

word = word.lower()

drow = word[::-1]

if word != drow:
    print("It's palindrome")
else:
    print("It's not palindrome")
