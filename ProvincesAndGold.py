gold, silver, copper = map(int, input().split())
totalValue = (gold * 3) + (silver * 2) + (copper * 1)
properties = ""
if totalValue >= 8:
    properties = "Province"
elif totalValue >= 5:
    properties = "Duchy"
elif totalValue >= 2:
    properties = "Estate"
else:
    properties = ""
if properties == "":
    if totalValue >= 6:
        print("Gold")
    elif totalValue >= 3:
        print("Silver")
    elif totalValue >= 0:
        print("Copper")
elif properties:
    if totalValue >= 6:
        print(properties + " or Gold")
    elif totalValue >= 3:
        print(properties + " or Silver")
    elif totalValue >=0:
        print(properties + " or Copper")