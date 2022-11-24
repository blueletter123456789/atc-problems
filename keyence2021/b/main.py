n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = [-1] * k
prev = 0
ri = 0
for ai in a:
    if prev != ai:
        prev = ai
        ri = 0
    if ri >= k:
        continue
    if ai - 1 == cnt[ri]:
        cnt[ri] = ai
    ri += 1

ans = 0
for num in cnt:
    ans += num + 1

print(ans)
