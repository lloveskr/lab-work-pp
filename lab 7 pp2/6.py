import re

with open('row.txt', 'r') as file:
    for line in file:
        result = re.sub(r'[ ,.]', ':', line)
        print(result.strip())