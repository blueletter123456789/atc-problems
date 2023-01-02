from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

points = []

n = int(input())
for _ in range(n):
    point = map(int, input().split())
    points.append(Point(*point))

is_line = False
for idx_a in range(n):
    for idx_b in range(idx_a+1, n):
        for idx_c in range(idx_b+1, n):
            a, b, c = points[idx_a], points[idx_b], points[idx_c]
            cross = (a.x-b.x) * (c.y-b.y) - (a.y-b.y) * (c.x-b.x)
            if cross == 0:
                is_line = True
                break
        if is_line:
            break
    if is_line:
        break

print('Yes' if is_line else 'No')
