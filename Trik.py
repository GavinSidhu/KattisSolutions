order = list(input())
placement = [1,0,0]
i = 0
t = 0
while i < len(order):
    if order[t] == "A":
        placement[0], placement[1] = placement[1], placement[0]
    if order[t] == "B":
        placement[1], placement[2] = placement[2], placement[1]
    if order[t] == "C":
        placement[0], placement[2] = placement[2], placement[0]
    t = t + 1
    i = i + 1
if placement[0] == 1:
    print("1")
elif placement[1] == 1:
    print("2")
elif placement[2] == 1:
    print("3")