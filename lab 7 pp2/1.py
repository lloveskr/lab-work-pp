import re

with open('row.txt', 'r') as file:
    for line in file:
        if re.search(r'ab*', line):
            print(line.strip())