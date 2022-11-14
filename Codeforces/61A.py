n1 = input()
n2 = input()

final = ''

for i in range(len(n1)):
    if n1[i] != n2[i]:
        final = final + '1'
    else:
        final = final + '0'

print(final)