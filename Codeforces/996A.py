dollars = int(input())

bills = 0

while dollars > 0:
    if dollars >= 100:
        bills += (dollars // 100)
        dollars %= 100
    if dollars >= 20:
        bills += (dollars // 20)
        dollars %= 20
    if dollars >= 10:
        bills += (dollars // 10)
        dollars %= 10
    if dollars >= 5:
        bills += (dollars // 5)
        dollars %= 5
    else:
        bills += dollars
        dollars = 0

print(bills)