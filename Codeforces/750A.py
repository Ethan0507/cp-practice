ips = [int(i) for i in input().split(" ")]
n, k = ips[0], ips[1]

curr_time = 0
# 4 hours ===> 240
reqd_time = 240 - k
i = 1
while i <= n and curr_time < reqd_time:
    next_q = 5 * i
    curr_time += next_q
    i += 1
if curr_time > reqd_time:
    print(i - 2)
else:
    print(i - 1)