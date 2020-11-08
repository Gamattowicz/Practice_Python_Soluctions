import json
from collections import Counter

with open('birthdays.json', 'r') as f:
    birth = json.load(f)

num = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

months = []

for date in birth.values():
    month = int(date[3:5])
    months.append(num[month-1])


print(Counter(months))
