d, n = map(int, input().split())

k = [1, 100, 10000]

ans = 1
if n == 100:
    ans = k[d]*(n+1)
else:
    ans = k[d]*n

print(ans)
