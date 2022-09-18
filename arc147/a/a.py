from collections import deque

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0
que = deque(a)
while len(que) > 1:
    min_n, max_n = que[0], que.pop()
    if max_n % min_n != 0:
        que.appendleft(max_n % min_n)
    ans += 1

print(ans)
