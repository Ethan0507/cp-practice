n = int(input())
gifts = [int(i) for i in input().split(" ")]
returned = [0] * n

for i in range(n):
    returned[gifts[i] - 1] = str(i + 1)

print(" ".join(returned))