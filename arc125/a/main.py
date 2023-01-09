n, m = map(int, input().split())

s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = 0
idxes = [-1, -1]
for i in range(n//2 + 1):
    if idxes[s[i]] < 0:
        idxes[s[i]] = i
    if idxes[s[(-i) % n]] < 0:
        idxes[s[(-i) % n]] = i

flg = s[0]
seen = False
for num in t:
    if flg != num and idxes[num] < 0:
        ans = -1
        break
    if flg != num:
        if not seen and idxes[num]:
            ans += idxes[num]
            seen = True
        else:
            ans += 1
        flg = num
    ans += 1

print(ans)
