from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    x = int(input())
    cnt[x] += 1

ans = 0
for num in cnt.values():
    if num % 2:
        ans += 1

print(ans)
