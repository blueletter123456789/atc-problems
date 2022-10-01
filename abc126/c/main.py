n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    if i >= k:
        ans += 1 / n
        continue
    
    j = 1
    while i * (2**j) < k:
        j += 1
    ans += 1 / n * 0.5**j

print('{:.12f}'.format(ans))
