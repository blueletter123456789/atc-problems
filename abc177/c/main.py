n = int(input())
a = list(map(int, input().split()))

M = 10**9 + 7
part = [0]*n
part[0] = a[0]
for i in range(1, n):
    part[i] = part[i-1] + a[i]

ans = 0
for i in range(n):
    ans += (a[i] * (part[-1] - part[i]) % M) % M
    ans %= M

print(ans)
