dims = [int(i) for i in input().split()]
grid = []
for i in range(dims[0]):
    curr = []
    for j in range(dims[1]):
        curr.append('.')
    grid.append(curr)
start = -1

for i in range(dims[0]):
    if i %  2 == 0:
        for j in range(dims[1]):
            grid[i][j] = '#'
    else:
        grid[i][start] = '#'
        if start == -1:
            start = 0
        else:
            start = -1

for i in range(dims[0]):
    print(''.join(grid[i]))