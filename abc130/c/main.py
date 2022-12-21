w, h, x, y = map(int, input().split())

area = h * w / 2
is_exist = 1 if h == y*2 and w == x*2 else 0

print(area, is_exist)
