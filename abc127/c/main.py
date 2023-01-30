n, m = map(int, input().split())
lst = [0] * (n + 2)
for _ in range(m):
    l, r = map(int, input().split())
    lst[l] += 1
    lst[r+1] -= 1

ans = 0
sum_num = 0
for cnt in lst:
    sum_num += cnt
    if sum_num >= m:
        ans += 1

print(ans)

# 下のように最小と最大を求めれる
# max_l = 0
# min_r = n
# for _ in range(m):
#     l, r = map(int, input().split())
#     max_l = max(max_l, l)
#     min_r = min(min_r, r)

# print(max(min_r - max_l + 1, 0))
