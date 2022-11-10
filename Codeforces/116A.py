maxCap = -1
curr = 0
for i in range(int(input())):
    inAndOut = [int(k) for k in input().split(" ")]
    curr -= inAndOut[0]
    curr += inAndOut[1]
    if curr > maxCap:
        maxCap = curr
print(maxCap)