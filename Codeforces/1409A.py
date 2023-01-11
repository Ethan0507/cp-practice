def getMoves(a, b):
    moves = 0
    while (b - a) > 0:
        diff =  b - a
        if diff > 10:
            a += ((diff // 10) * 10)
            moves += (diff // 10)
        else:
            a = b
            moves += 1
    return moves

for t in range(int(input())):
    inputs = [int(i) for i in input().split()]
    a, b = inputs[0], inputs[1]

    if b > a:
        moves = getMoves(a, b)
    else:
        moves = getMoves(b, a)
    print(moves)