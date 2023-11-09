import re

with open('row.txt', 'r') as file:
    for line in file:
        matches = re.findall(r'[a-z]+_[a-z]+', line)
        for match in matches:
            print(match)