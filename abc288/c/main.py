from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 0

seen = [-1] * n
for i in range(n):
    if seen[i] >= 0:
        continue
    que = deque([(i, -1)])
    seen[i] = 0

    while len(que):
        cur, prev = que.popleft()

        for v in G[cur]:
            if seen[v] < 0:
                seen[v] = seen[cur] + 1
                que.append((v, cur))
                continue
            if seen[v] >= 0 and v != prev:
                ans += 1

print(ans // 2)

# 全域木を辿り、辺の本数から差分をとる
# 連結成分の個数をカウントし、辺の本数、頂点の数との差分をとる
