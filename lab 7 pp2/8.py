import re

with open('row.txt', 'r') as file:
    for line in file:
        result = re.findall('[A-Z][a-z]*', line)
        for match in result:
            print(match)