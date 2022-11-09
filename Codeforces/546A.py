inputs = input().split()
k, n, w = int(inputs[0]), int(inputs[1]), int(inputs[2])
i = 1

while i <= w:
    n -= i * k
    i += 1

if n < 0:
    print(n * -1)
else:
    print(0)