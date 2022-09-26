n, m = map(int, input().split())
solved = [input() for _ in range(n)]

odds = 0
evens = 0
for s in solved:
    cnt = 0
    for si in s:
        if si == "1":
            cnt += 1
    
    if cnt % 2:
        odds += 1
    else:
        evens += 1

print(odds * evens)
