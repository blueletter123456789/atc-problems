n = int(input())

march = 'MARCH'
chars = {k: 0 for k in list(march)}
for _ in range(n):
    s = input()[0]
    if s in march:
        chars[s] += 1

ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += chars[march[i]]*chars[march[j]]*chars[march[k]]

print(ans)
