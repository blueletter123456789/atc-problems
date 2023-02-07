n, m = map(int, input().split())

G = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    G[v].add(u)

seen = set()
for a in range(n):
    for b in G[a]:
        same = G[a] & G[b]
        for c in same:
            col = tuple(sorted((a, b, c)))
            if col in seen:
                continue
            seen.add(col)

print(len(seen))
