a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())

x=a2-a1
y=b2-b1
if x<0: x=x*-1
if y<0: y=y*-1
if(x==y): print('YES')
else: print('NO')