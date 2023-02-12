from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

que = deque()
ans = []
i = 0
for j in range(1, n+1):
    que.append(str(j))
    if not m or j != a[i]:
        while len(que):
            ans.append(que.pop())
    else:
        i += 1
        i = min(i, m - 1)

while len(que):
    ans.append(que.pop())

print(' '.join(ans))
