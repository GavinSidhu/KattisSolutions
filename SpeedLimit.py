speedChange = int(input())
while speedChange > -1:
    i = 0
    total = 0
    t = 0
    while i < speedChange:
        x, y = map(int, input().split())
        total = total + (x * (y - t))
        t = y
        i = i + 1
    print(str(total) + " miles")
    speedChange = int(input())

                 
