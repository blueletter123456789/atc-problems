n = bin(int(input()))[2:]

idx = []
for i, chr in enumerate(reversed(n)):
    if chr == '1':
        idx.append(i)

for i in range(1 << len(idx)):
    ans = 0
    for j in range(len(idx)):
        if i & (1 << j):
            ans += (1 << idx[j])
    print(ans)
