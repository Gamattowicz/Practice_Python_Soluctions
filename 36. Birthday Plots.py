import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


with open('scientist_birthdays.json', 'r') as f:
    birth = json.load(f)

num = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

months = []

for date in birth.values():
    month = int(date[0:2])
    months.append(num[month-1])

base = Counter(months)

output_file("plot.html")
x_categories = num

x = list(base.keys())
y = list(base.values())

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)
