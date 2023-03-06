from collections import defaultdict


n, q = map(int, input().split())

cnt = defaultdict(list)
for idx, a in enumerate(input().split()):
    cnt[int(a)].append(idx + 1)

for _ in range(q):
    x, k = map(int, input().split())
    if x not in cnt or len(cnt[x]) < k:
        print(-1)
        continue
    print(cnt[x][k-1])
