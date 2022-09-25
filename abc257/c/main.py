n = int(input())
s = input()
w = list(map(int, input().split()))
pairs = list()
cnt = 0
for wi, si in zip(w, s):
    pairs.append((wi, si))
    if si == '1':
        cnt += 1

pairs.sort()
ans = cnt
for i in range(n):
    wi, si = pairs[i]
    if si == '0':
        cnt += 1
    else:
        cnt -= 1
    if i+1 < n and pairs[i][0] != pairs[i+1][0]:
        ans = max(ans, cnt)
    elif i == n-1:
        ans = max(ans, cnt)

print(ans)
