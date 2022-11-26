# from collections import deque

# n, q = map(int, input().split())

# G = [[] for _ in range(n)]
# for _ in range(n):
#     a, b = map(int, input().split())
#     G[a-1].append(b-1)
#     G[b-1].append(a-1)

# dist = [[-1, float('inf')] for _ in range(n)]
# dist[0][1] = 0
# que = deque([0])
# while len(que):
#     current = que.popleft()
#     _, cur_dist = dist[current]
    
#     for e in G[current]:
#         if dist[e][1] > cur_dist + 1:
#             dist[e] = [current, cur_dist + 1]
#             que.append(e)

# for i in range(q):
#     c, d = map(int, input().split())

from collections import deque

n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [-1]*n
dist[0] = 0
que = deque([0])
while len(que):
    current = que.popleft()
    for e in G[current]:
        if dist[e] == -1:
            dist[e] = 1 - dist[current]
            que.append(e)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
