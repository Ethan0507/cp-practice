n = int(input())
scores = [int(i) for i in input().split(" ")]

minScore, maxScore = scores[0], scores[0]
count = 0
for i in range(1, len(scores)):
    if scores[i] < minScore:
        count += 1
        minScore = scores[i]
    if scores[i] > maxScore:
        count += 1
        maxScore = scores[i]
    
print(count)