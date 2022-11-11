year = int(input())

while year < 9013:
    year += 1
    if len(set(str(year))) == 4:
        print(year)
        break