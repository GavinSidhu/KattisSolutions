hour, minute = map(int, input().split())
if (hour > 0):
    if minute > 45:
        print(str(hour) + " " + str(minute - 45))
    elif minute < 45:
        newMinute = 45 - minute
        print(str(hour - 1) + " " + str(60 - newMinute))
    else:
        print(str(hour) + " 00")
elif(hour == 0):
    if minute > 45:
        print(str(hour) + " " + str(minute - 45))
    elif (minute < 45):
        newMinute = 45 - minute
        print("23 " + str(60-newMinute))
    else:
        print("23 00")