n = int(input())
min_num = float('inf')
for _ in range(5):
    min_num = min(min_num, int(input()))

ans = 5 + n//min_num
if n % min_num == 0:
    ans -= 1
print(ans)
