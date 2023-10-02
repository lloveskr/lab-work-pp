n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for b in range(n):
    for j in range(b + 1, n):
        if x[b] == x[j] or y[b] == y[j] or abs(x[b] - x[j]) == abs(y[b] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')