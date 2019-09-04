monthlyMegabyte = int(input())
numMonths = int(input())
dataAllotted = monthlyMegabyte * numMonths
dataAllotted = dataAllotted + monthlyMegabyte
month = 1
total = 0
while (month < numMonths + 1):
    total += int(input())
    month += 1
print(dataAllotted - total)