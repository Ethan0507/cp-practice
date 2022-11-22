for i in range(int(input())):
    ips = [int(j) for j in input().split(" ")]
    a, b  = ips[0], ips[1]
    if (a % b == 0):
        print(0)
    else:
        n = (a // b) + 1
        print((b * n) - a)