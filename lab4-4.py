input_sequence = list(map(int, input().split()))
seen_n = {}  

for number in input_sequence:
    if number in seen_n:
        print("YES")
    else:
        print("NO")
        seen_n[number] = True