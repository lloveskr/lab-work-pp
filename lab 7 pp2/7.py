import re

with open('row.txt', 'r') as file:
    for line in file:
        snake_case = line.strip()
        camel_case = ''.join(word.capitalize() for word in snake_case.split('_'))
        print(camel_case)