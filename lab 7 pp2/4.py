import re

with open('row.txt', 'r') as file:
    for line in file:
        matches = re.findall(r'[A-Z][a-z]+', line)
        for match in matches:
            print(match)