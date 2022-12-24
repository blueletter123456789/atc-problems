def calc_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


n, m = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

for xi, yi in zip(x, y):
    min_dist = float('inf')
    ans = 0
    for idx, (xj, yj) in enumerate(zip(a, b)):
        c = calc_dist(xi, yi, xj, yj)
        if min_dist > c:
            ans = idx + 1
            min_dist = c
    print(ans)
