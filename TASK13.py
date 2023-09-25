A=int(input())
D=int(input())
x=int(input())
y=int(input())
max=A
min=D
if(min>max): min=A
if(min==A): max=D

if(min/2>x): mind1=x
else: mind1=min-x
if(max/2>y): mind2=y
else: mind2=max-y

if(mind1<mind2): print(mind1)
else: print(mind2)