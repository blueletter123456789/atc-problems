n = int(input())

ans = [[-1]*n for _ in range(n)]
num = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if not (i + j) % 2:
            ans[i-1][j-1] = num
            num += 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i + j) % 2:
            ans[i-1][j-1] = num
            num += 1

for row in ans:
    print(' '.join([str(i) for i in row]))
