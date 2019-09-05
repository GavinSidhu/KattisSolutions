from math import sqrt
total, height, width = map(int, input().split())
i = 1
hypotenuse = sqrt((width**2) + (height**2))
while i <= total:
    test = int(input())
    if test <= height:
        print("DA")
    elif test <= width:
        print("DA")
    elif test <= hypotenuse:
        print("DA")
    else:
        print("NE")
    i += 1