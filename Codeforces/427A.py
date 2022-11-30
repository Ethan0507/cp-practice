n = int(input())
series = [int(i) for i in input().split(" ")]

curr_recruits = 0
crimes = 0
for i in series:
    if i > 0:
        curr_recruits += i
    else:
        if curr_recruits != 0:
            curr_recruits -= 1
        else:
            crimes += 1

print(crimes)