atBat = int(input())
hits = list(map(float, input().split()))
total = 0
for hit in hits:
    if hit > 0:
        total = total + hit
average = total / atBat
print(average)