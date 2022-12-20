from collections import defaultdict


n, k = map(int, input().split())
a = list(map(int, input().split()))

seen = defaultdict(int)
for num in a:
    seen[num] += 1

seen = sorted(seen.items(), key=lambda x: x[1])
ans = 0
for i in range(len(seen)-k):
    ans += seen[i][1]

print(ans)
