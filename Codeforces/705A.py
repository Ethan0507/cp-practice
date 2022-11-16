n = int(input())
feelings = ''

for i in range(n):
    if i % 2 == 0:
        feelings = feelings + 'I hate'
    else:
        feelings = feelings + 'I love'
    if i < n - 1:
        feelings = feelings + ' that '

feelings = feelings + ' it'
print(feelings)