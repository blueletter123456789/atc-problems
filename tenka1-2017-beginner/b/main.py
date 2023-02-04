n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.append((1, float('inf')))

lst.sort(key=lambda x: x[1])
prev_idx = float('inf')
prev_num = -1
ans = 0
for a, b in lst:
    ans += min(prev_idx - a, b - prev_num)
    prev_idx, prev_num = a, b

print(ans)
