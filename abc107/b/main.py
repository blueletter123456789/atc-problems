h, w = map(int, input().split())

a = []
for _ in range(h):
    s = input()
    if s != '.' * w:
        a.append(s)

ans = [[] for _ in range(len(a))]
for i in range(w):
    is_white = True
    for j in range(len(a)):
        if a[j][i] == '#':
            is_white = False
            break
    if not is_white:
        for j in range(len(a)):
            ans[j].append(a[j][i])

for row in ans:
    print(''.join(row))
