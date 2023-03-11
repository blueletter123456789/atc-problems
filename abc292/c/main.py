from collections import defaultdict

n = int(input())

nums = defaultdict(int)
for i in range(1, int(n**0.5) + 1):
    for j in range(i, n//i+1):
        num = 2
        if i == j:
            num -= 1
        nums[i*j] += num

ans = 0
for ab in range(1, n):
    cd = n - ab
    ans += nums[ab] * nums[cd]

print(ans)
