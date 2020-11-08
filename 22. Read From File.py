count = {}

with open('Training_01.txt', 'r') as file:
    for line in file:
        line = line[3:-26]
        line = line.strip()
        if line in count:
            count[line] += 1
        else:
            count[line] = 1
    for pair in count.items():
        print(pair)
