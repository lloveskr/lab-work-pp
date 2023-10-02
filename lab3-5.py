l = [int(a) for a in input().split()]
cnt = 0
for a in range(1, len(l) - 1):
    if l[a - 1] < l[a] > l[a + 1]:
        cnt += 1
print(cnt)