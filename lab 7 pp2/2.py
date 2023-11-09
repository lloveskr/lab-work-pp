import re

with open('row.txt', 'r') as file:
    for line in file:
        if re.search(r'ab{2,3}', line):
            print(line.strip())