ips = [int(i) for i in input().split()]
a, b = ips[0], ips[1]

diffSocks = min(a, b)
sameSocks = (max(a, b) - min(a, b)) // 2

print(diffSocks, sameSocks)