xS = [int(i) for i in input().split()]
abc = max(xS)

numbers = []

for i in xS:
    if i != abc:
        numbers.append(str(abc - i))

print(' '.join(numbers))