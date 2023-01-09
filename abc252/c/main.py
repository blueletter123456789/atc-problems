n = int(input())

s = [input() for _ in range(n)]
min_time = float('inf')
for i in range(10):
    times = [[0, i] for i in range(10)]
    for row in s:
        for idx, num in enumerate(row):
            if int(num) == i:
                times[idx][0] += 1
    times.sort()
    cost = (times[-1][0] - 1) * 10 + times[-1][1]
    min_time = min(min_time, cost)

print(min_time)
