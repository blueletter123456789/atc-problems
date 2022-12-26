n = int(input())
s = list(input())
q = int(input())

st = 0
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        ai = (st + a - 1) % (n * 2)
        bi = (st + b - 1) % (n * 2)
        s[ai], s[bi] = s[bi], s[ai]
    elif t == 2:
        st += n
        st %= n * 2

ans = []
if st:
    ans = s[st:] + s[:st]
else:
    ans = s

print(''.join(str(c) for c in ans))
