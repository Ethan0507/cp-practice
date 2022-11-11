inps = [int(i) for i in input().split(" ")]
friends = [int(i) for i in input().split(" ")]

for i in friends:
    if i > inps[1]:
        inps[0] += 1

print(inps[0])