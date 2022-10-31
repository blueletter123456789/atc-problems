n = int(input())

ans = float('inf')
i = 1
while i * i <= n:
    if n % i == 0:
        ans = min(ans, (i + n//i - 2))
    i += 1

print(ans)
