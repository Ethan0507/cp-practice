word = input()
uppers = 0

for char in word:
    if char.isupper():
        uppers += 1

if uppers > len(word) // 2:
    print(word.upper())
else:
    print(word.lower())