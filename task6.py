a=int(input())
d=int(input())
c=int(input())

if(a==d) and (a==c) and (d==c):
    print(3)
elif(a==d) or (a==c) or (d==c):
    print(2)
else: print(0)