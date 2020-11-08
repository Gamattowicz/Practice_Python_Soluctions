txt = input()

new = txt.split(' ')

this = 'a'

for i in range(0, len(new)):
    if len(new[i]) > len(this):
        this = new[i]

print(this)
