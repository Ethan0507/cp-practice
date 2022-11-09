inputs = input().split()
n, k = int(inputs[0]), int(inputs[1])

while k > 0:
    if n % 10 != 0:
        n -= 1
    else:
        n //= 10
    k -= 1

print(n)