import re

with open('row.txt', 'r') as file:
    for line in file:
        camel_case = line.strip()
        snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
        print(snake_case)