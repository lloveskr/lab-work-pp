input1 = set(map(int, input().split()))
input2 = set(map(int, input().split()))
result = sorted(input1 & input2)
print(*result)
