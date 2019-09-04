number = int(input())
temp = list(map(int,input().split()))
total = 0
for t in temp:
    if t < 0:
        total += 1
print(total)