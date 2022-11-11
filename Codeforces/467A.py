count = 0
for i in range(int(input())):
    accom = [int(j) for j in input().split(" ")]
    if accom[1] - accom[0] >= 2:
        count += 1
print(count)