n = int(input())
count = 1

prev = input()
for i in range(n - 1):
    curr = input()
    if curr[0] == prev[1]:
        count += 1
    prev = curr

print(count)