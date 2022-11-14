dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

h, w = map(int, input().split())
s = list()
for _ in range(h):
    s.append(input())

is_draw = True
for y in range(h):
    for x in range(w):
        if s[y][x] != '#':
            continue
        next_cell = False
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if s[ny][nx] == '#':
                next_cell = True
                break
        if not next_cell:
            is_draw = False
            break

    if not is_draw:
        break

print('Yes' if is_draw else 'No')
