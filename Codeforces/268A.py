from collections import defaultdict

jerseys = [[0, 0]] * int(input())

jerseyTally = defaultdict(list)

for i in range(len(jerseys)):
    jerseys[i] = [int(j) for j in input().split(" ")]
    if jerseyTally[jerseys[i][0]]:
        jerseyTally[jerseys[i][0]][0] += 1
    else:
        jerseyTally[jerseys[i][0]] = [1, 0]
    if jerseyTally[jerseys[i][1]]:
        jerseyTally[jerseys[i][1]][1] += 1
    else:
        jerseyTally[jerseys[i][1]] = [0, 1]

count = 0
for i, j in jerseyTally.values():
    count += (i * j)

print(count)