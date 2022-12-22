import sys

sys.setrecursionlimit(10**6)


def dfs(cur, t, seen):
    if cur == t:
        return True, []
    seen[cur] = 1
    res, ans = False, []
    for nxt in G[cur]:
        if seen[nxt]:
            continue
        res, ans = dfs(nxt, t, seen)
        if res:
            ans.append(nxt)
            break
    return res, ans


n, x, y = map(int, input().split())
x -= 1
y -= 1

G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [0] * n
_, ans = dfs(x, y, seen)
ans.append(x)

print(' '.join([str(i+1) for i in reversed(ans)]))
