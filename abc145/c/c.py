import math
import itertools

def two_dist(a, b):
    xi = x[a] - x[b]
    yi = y[a] - y[b]
    return math.sqrt(xi**2 + yi**2)

n = int(input())
x, y = [0]*n, [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

dist = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = two_dist(i, j)

perms = 1
for i in range(1, n+1):
    perms *= i

ans = 0
for i, perm in enumerate(itertools.permutations(range(n))):
    for i in range(n-1):
        ans += dist[perm[i+1]][perm[i]]

print(ans / perms)
