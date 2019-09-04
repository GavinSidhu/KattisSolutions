x, y = map(int,input().split())
highestCount = x + y
if (x == y):
    print(x+1)
else:
    numAnswers = abs(x-y) + 1
    last = min(x,y) + numAnswers + 1
    start = min(x,y) + 1
    for i in range(start, last):
        print(i)