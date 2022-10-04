M = 998244353

n = int(input())

ans = 0
min_k, max_k = 0, 10
while n > 0:
    if min_k > n:
        break
    elif min_k <= n < max_k:
        k = (n - min_k) % max_k
    else:
        k = (max_k - 1) - min_k
    
    ans += (k * (k + 1) // 2) % M
    ans %= M

    min_k = max_k - 1
    max_k *= 10

print(ans)
