from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

num_range = defaultdict(int)
for i in a:
    num_range[i-1] += 1
    num_range[i] += 1
    num_range[i+1] += 1

ans = 0
for i in num_range.values():
    ans = max(ans, i)

print(ans)
