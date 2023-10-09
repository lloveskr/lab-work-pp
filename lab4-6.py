n = int(input())

unique_words = set()

for _ in range(n):
    line = input()
    words = line.split()
    
    unique_words.update(words)


print(len(unique_words))