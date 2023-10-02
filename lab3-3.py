l=input().split()
for a in range(1,len(l)):
    if l[a]>l[a-1]:
        print(l[a])