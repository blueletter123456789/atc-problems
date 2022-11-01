n = int(input())

ans = True
prev_t, prev_x, prev_y = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    dist = abs(x-prev_x)+abs(y-prev_y)
    duration = abs(t-prev_t)
    if dist > duration or dist % 2 != duration % 2:
        ans = False
        break
    prev_t, prev_x, prev_y = t, x, y

print('Yes' if ans else 'No')
