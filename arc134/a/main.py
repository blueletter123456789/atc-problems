n, l, w = map(int, input().split())

prev = 0
ans = 0
for a in (int(i) for i in input().split()):
    if prev < a:
        ans += (a - prev + (w - 1)) // w
    prev = a + w

if prev < l:
    ans += (l - prev + (w - 1)) // w

print(ans)
