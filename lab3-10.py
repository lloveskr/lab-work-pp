a = [int(b) for b in input().split()]
for b in range(1, len(a), 2):
    a[b - 1], a[b] = a[b], a[b - 1]
print(' '.join([str(b) for b in a]))