from collections import Counter, defaultdict

l1 = input()
l2 = input()
pile = input()

countOfChars = Counter(pile)
countOfLets = Counter(l1 + l2)

if countOfChars == countOfLets:
    print("YES")
else:
    print("NO")