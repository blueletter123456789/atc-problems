n, k = map(int, input().split())

rate = dict()
max_num = n*2 + 2

cnt = 1
for i in range(2, max_num//2):
    rate[i] = cnt
    rate[max_num-i] = cnt
    cnt += 1
rate[max_num//2] = cnt

ans = 0
for i in range(2, 2*n+1):
    tgt = i - k
    if 2 <= tgt <= n*2:
        ans += rate[i] * rate[tgt]

print(ans)
