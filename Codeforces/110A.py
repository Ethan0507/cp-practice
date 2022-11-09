def isnearlyLucky(num):
    if num < 4:
        return False
    while num > 0:
        if num % 10 != 4 and num % 10 != 7:
            return False
        num //= 10
    return True

num = input()

luckyNum = 0
for i in num:
    if i == '4' or i == '7':
        luckyNum += 1

if isnearlyLucky(luckyNum):
    print("YES")
else:
    print("NO")