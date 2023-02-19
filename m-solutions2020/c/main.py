from collections import deque


n, k = map(int, input().split())
lst = list(map(int, input().split()))
que = deque([i for i in lst[:k]])
for num in lst[k:]:
    prev = que.popleft()
    if prev < num:
        print('Yes')
    else:
        print('No')
    que.append(num)
