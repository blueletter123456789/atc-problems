n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << n):
    cnt = 1
    for j in range(n):
        if (1 << j) & i:
            if a[j] % 2:
                cnt *= 2
        else:
            if (a[j] % 2) == 0:
                cnt *= 2
    ans += cnt

print(ans)

"""
'3^n - 2^e'(e=(ai%2))で求めることができる
"""
