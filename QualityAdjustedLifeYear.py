num = int(input())
i = 0
total = 0
while (i < num):
    x, y = map(float,input().split())
    total = total + (x * y)
    i += 1
print(total)