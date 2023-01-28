from collections import deque

GOAL = 1

n = int(input())

G = []
for i in range(n):
    ai = int(input()) - 1
    G.append(ai)

que = deque([0])
dist = [-1] * n
dist[0] = 0

while len(que):
    current = que.popleft()
    e = G[current]
    if dist[e] > 0:
        break
    dist[e] = dist[current] + 1
    que.append(e)

print(dist[GOAL])
