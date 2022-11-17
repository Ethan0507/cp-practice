n = int(input())
soldiers = [int(i) for i in input().split(" ")]

minH, minHId = 10000, -1
maxH, maxHId = -1, -1

for i in range(n):
    if soldiers[i] > maxH:
        maxH = soldiers[i]
        maxHId = i
    if soldiers[i] <= minH:
        minH = soldiers[i]
        minHId = i

time = maxHId + (n - 1 - minHId)
if maxHId > minHId:
    time -= 1
print(time)