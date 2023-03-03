n, x = map(int, input().split())

reach = [[False] * (x + 1) for _ in range(n+1)]
reach[0][0] = True

for i in range(n):
    a, b = map(int, input().split())
    for j in range(x+1):
        if j >= a and reach[i][j-a]:
            reach[i+1][j] = True
        if j >= b and reach[i][j-b]:
            reach[i+1][j] = True

print('Yes' if reach[n][x] else 'No')
