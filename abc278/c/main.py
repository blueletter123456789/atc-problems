from collections import defaultdict

n, q = map(int, input().split())
follow = defaultdict(set)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        follow[a].add(b)
    elif t == 2:
        if b in follow[a]:
            follow[a].remove(b)
    else:
        print('Yes' if a in follow[b] and b in follow[a] else 'No')
