prime_num = set()
happy_num = set()

with open('primenumbers.txt', 'r') as prime_file:
    for i in prime_file:
        prime_num.add(int(i.strip()))

with open('happynumbers.txt', 'r') as happy_file:
    for j in happy_file:
        happy_num.add(int(j.strip()))

sum = list(set(prime_num) & set(happy_num))
sum.sort()
print(sum)
