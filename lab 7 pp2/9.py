import re

with open('row.txt', 'r') as file:
    for line in file:
        result = re.sub(r'([a-z])([A-Z])', r'\1 \2', line)
        print(result.strip())