num = int(input())
while num > 0:
    i = 1 
    t = 0
    total = 0
    while i <= num:
        x, y = map(int, input().split())
        total = total + (x * (y - t))
        t = y
        i += 1
    print(total)
            
