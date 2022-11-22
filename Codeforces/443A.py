from collections import defaultdict

aSet = input()
chars = defaultdict(int)
count = 0

for i in aSet:
    if i != '{' and i != ',' and i != ' ' and i != '}':
        if chars[i] != 1:
            count += 1
        chars[i] = 1

print(count)