a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())

if abs(a1 - a2) == abs(b1 - b2):
    print('YES')
elif a1==a2 or b1==b2:
    print('YES')
else:
    print('NO')