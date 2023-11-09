import re

with open('row.txt', 'r') as file:
    for line in file:
        if re.search(r'a.*b$', line):
            print(line.strip())