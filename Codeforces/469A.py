n = int(input())

levels = [0] * n

levelX = [int(i) for i in input().split(" ")]
levelY = [int(i) for i in input().split(" ")]

for i in range(1, levelX[0] + 1):
    levels[levelX[i] - 1] = 1

for i in range(1, levelY[0] + 1):
    levels[levelY[i] - 1] = 1

if levels == [1] * n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')