a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())

if a2==a1+1 or a2==a1-1:
    if b2==b1+2 or b2==b1-2:
        print('YES')
    else: print('NO')
elif b2==b1+1 or b2==b1-1:
    if a2==a1+2 or a2==a1-2:
        print('YES')
    else: print('NO')
else: print('NO')