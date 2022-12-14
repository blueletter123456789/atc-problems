n = input()

max_erase = float('inf')
for i in range(1, 1 << len(n)):
    tgt = ''
    cnt = 0
    for j in range(len(n)):
        if i & (1 << j):
            tgt += n[j]
        else:
            cnt += 1
    if (int(tgt) % 3) == 0:
        max_erase = min(cnt, max_erase)

print(max_erase if max_erase != float('inf') else -1)
