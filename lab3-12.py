a = [int(d) for d in input().split()]
k, C = [int(d) for d in input().split()]

a.append(0)
for b in range(len(a) - 1, k, -1):
    a[b] = a[b - 1]
a[k] = C
print(' '.join([str(b) for b in a]))