n = int(input())
x, y = [], []

for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ax, ay = x[i], y[i]
            bx, by = x[j], y[j]
            cx, cy = x[k], y[k]
            abx, aby = bx - ax, by - ay
            acx, acy = cx - ax, cy - ay
            if abx * acy - aby * acx == 0:
                continue
            cnt += 1

print(cnt)
