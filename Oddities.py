oddities = int(input())
i = 1
while i <= oddities:
    number = int(input())
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
    i += 1