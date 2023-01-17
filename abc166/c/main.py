n, m = map(int, input().split())
h = list(map(int, input().split()))
G = [i for i in h]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] > h[b]:
        G[b] = h[a]
    elif h[a] < h[b]:
        G[a] = h[b]
    elif h[a] == h[b]:
        G[a] = float('inf')
        G[b] = float('inf')

ans = 0
for i in range(n):
    if h[i] == G[i]:
        ans += 1

print(ans)
