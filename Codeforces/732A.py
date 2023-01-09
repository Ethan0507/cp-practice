ips = [int(i) for i in input().split()]
k, r, curr = ips[0], ips[1], ips[0]

if k % 10 == 5:
    if r == 5:
        print(1)
    else: 
        print(2)
else:
    n = 1
    while curr % 10 != r and curr % 10 != 0:
        n += 1
        curr = k * n

    print(n)