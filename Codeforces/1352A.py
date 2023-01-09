for i in range(int(input())):
    n = int(input())
    nSummands = 0
    summands = []
    d = 1

    while n > 0:
        if n % 10 != 0:
            nSummands += 1
            summands.append(str((n % 10) * d))
        n //= 10
        d *= 10
    
    print(nSummands)
    print(' '.join(summands))