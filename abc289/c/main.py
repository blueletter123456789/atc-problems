n, m = map(int, input().split())
s = []
for i in range(m):
    _ = input()
    a = list(map(int, input().split()))
    s.append(a)

ans = 0
for i in range(1 << m):
    cnt = set()
    for j in range(m):
        if (1 << j) & i:
            for num in s[j]:
                cnt.add(num)
    if len(cnt) == n:
        ans += 1

print(ans)
