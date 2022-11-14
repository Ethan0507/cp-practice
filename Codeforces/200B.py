n = int(input())

sumOrange = sum([int(i) for i in input().split(" ")])

print(round((sumOrange / (n * 100)) * 100, 12))