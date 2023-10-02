a = input().split() 
for b in range(len(a)-1):
    n = int(a[b]) 
    b += 1
    m = int(a[b]) 
    if (n * m) > 0:
        print(n, m, end=' ')
        break