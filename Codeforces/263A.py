from asyncio.windows_events import NULL


r, c = 0, 0
for i in range(5):
    row = input().split(" ")
    for j in range(len(row)):
        if row[j] == '1':
            r, c = i, j

print(abs(2 - r) + abs(2 - c))