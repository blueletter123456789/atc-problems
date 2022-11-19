from collections import defaultdict


direction = {'R': 'L', 'L': 'R'}

n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
s = input()

ans = False
seen = defaultdict(dict)
for si, xi, yi in zip(s, x, y):
    if si not in seen[yi]:
        seen[yi][si] = xi
    if si == 'R':
        if direction[si] not in seen[yi] or seen[yi][direction[si]] < xi:
            seen[yi][si] = min(seen[yi][si], xi)
        else:
            ans = True
            break
    else:
        if direction[si] not in seen[yi] or seen[yi][direction[si]] > xi:
            seen[yi][si] = max(seen[yi][si], xi)
        else:
            ans = True
            break

print('Yes' if ans else 'No')
