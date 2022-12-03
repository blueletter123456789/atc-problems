n, s, t = map(int, input().split())
w = 0

cnt = 0
for _ in range(n):
    a = int(input())
    w = max(w+a, 0)
    if s <= w <= t:
        cnt += 1

print(cnt)
