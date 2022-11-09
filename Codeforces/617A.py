dist = int(input())
steps = 0

while dist > 5:
    steps += 1
    dist -= 5

print(steps + 1)