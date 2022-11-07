ages = input().split(" ")
a, b = int(ages[0]), int(ages[1])
i = 0

while a <= b:
    a *= 3
    b *= 2
    i += 1

print(i)