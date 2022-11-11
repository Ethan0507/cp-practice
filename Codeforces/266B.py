inps = [int(i) for i in input().split(" ")]
queue = input()
secs = 0

while secs < inps[1]:
    i = 0
    new_queue = ''
    while i < inps[0]:
        if i != inps[0] -1 and queue[i] == 'B' and queue[i + 1] == 'G':
            new_queue += 'GB'
            i += 2
        else:
            new_queue += queue[i]
            i += 1
    queue = new_queue
    secs += 1
print(new_queue)