import random 

a = list(random.sample(range(30), 10 + random.randrange(4)))
b = list(random.sample(range(40), 10 + random.randrange(6)))

a.sort()
b.sort()

c = list(set(a) & set(b))

c.sort()

print('List a: {}, list b: {} and list c: {}'.format(a, b, c))
