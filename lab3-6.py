imax = 0
a = [int(b) for b in input().split()]
for b in range(1, len(a)):
    if a[b] > a[bmax]:
        bmax = b
print(a[bmax], bmax)