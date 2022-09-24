from itertools import permutations

n, k = map(int, input().split())
route = list()
for _ in range(n):
    route.append(list(map(int, input().split())))

ans = 0
for p in permutations(range(n-1)):
    path = 0
    prev = 0
    for i in p:
        path += route[prev][i+1]
        prev = i+1
    
    path += route[prev][0]
    if path == k:
        ans += 1

print(ans)
