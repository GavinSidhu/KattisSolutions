string = input()
upper = []
for character in string:
    if character.isupper():
        upper.append(character)
print("".join(upper))