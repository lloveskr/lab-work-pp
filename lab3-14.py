a = [int(b) for b in input().split()]
for d in range(len(a)):
    for j in range(len(a)):
        if d != j and a[d] == a[j]:
            break
    else:
        print(a[d], end=' ')