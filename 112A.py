string1 = input()
string2 = input()
eq = True

for i in range(len(string1)):
    if ord(string1[i].lower()) < ord(string2[i].lower()):
        print(-1)
        eq = False
        break
    elif ord(string1[i].lower()) > ord(string2[i].lower()):
        print(1)
        eq = False
        break

if eq:
    print(0)