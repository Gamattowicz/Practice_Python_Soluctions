birthday = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

print('''Welcome to the birthday dictionary program.
We know date of birthday of:''')
for name in birthday:
    print(name)
choice = input("Who's birthday do you wanna know? ")
if choice in birthday:
    print('{} was born in {}'.format(choice, birthday[choice]))
else:
    print("We don't have date of birtday {} in our datebase".format(choice))
