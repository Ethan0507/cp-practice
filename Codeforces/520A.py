n = int(input())
sent = input()

al = [0] * 26

if n < 26:
    print("NO")
else:
    for i in sent:
        al[ord(i.lower()) % 97] = 1
    if sum(al) == 26:
        print("YES")
    else:
        print("NO")