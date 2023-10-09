N, K = [int(i) for i in input().split()]
A = set()
mass = [[int(i) for i in input().split()] for j in range(K)]
for i in range(K):
    day = mass[i][0]
    start = mass[i][0]
    step = mass[i][1]
    while day <= N:
        if day % 7 != 0 and day % 7 != 6:
            A.add(day)
        day += step
print(len(A))