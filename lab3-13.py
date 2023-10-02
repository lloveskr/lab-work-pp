a = [int(b) for b in input().split()]
cnt = 0
for d in range(len(a)):
    for j in range(d + 1, len(a)):
        if a[d] == a[j]:
            cnt += 1
print(cnt)