a, d = 0, 0
n = int(input())
for i in input():
    if i == 'A':
        a += 1
    else:
        d += 1
if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")