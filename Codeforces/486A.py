n = int(input())

if n % 2 == 0:
    newN = n // 2
else:
    newN = (n // 2) + 1

sumP = (n // 2) * ((n // 2) + 1)
sumN = newN ** 2

print(sumP - sumN)