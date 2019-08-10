import re

with open("/home/brady/Downloads/stylist.html") as f:
    for line in f:
        if re.search("div id=\"n", line):
            line = line.strip()
            print(line)
