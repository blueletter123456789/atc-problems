x, k, d = map(int, input().split())

x = abs(x)
init_cnt = min(k, x//d)
dist = x - init_cnt * d
k -= init_cnt

dist -= d * (k % 2)

print(abs(dist))
