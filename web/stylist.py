import re

with open("/home/brady/Downloads/stylist.html") as f:
    items = []
    for line in f:
        if re.search("div id=\"n", line):
            line = line.strip()
            pieces = line.split(" ")
            n = pieces[1]
            color = pieces[3]
            a, b = color[5], color[6]
            h = a + b
            item = [n, h]
            items.append(item)
    items.sort(key=lambda tup: tup[0])
    print(items)
