from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

kinds = defaultdict(int)
for i in c[:k]:
    kinds[i] += 1

ans = len(kinds)
for i, num in enumerate(c[k:]):
    kinds[num] += 1
    kinds[c[i]] -= 1
    if kinds[c[i]] <= 0:
        del kinds[c[i]]
    ans = max(ans, len(kinds))

print(ans)
