t, n = map(int, input().split())


seen = set()
for i in range(1, 100 + t + 1):
    seen.add(i * (100 + t) // 100)

not_exists = []
for i in range(1, 100 + t + 1):
    if i not in seen:
        not_exists.append(i)

idx = (n - 1) % len(not_exists)
ans = not_exists[idx] + ((n - 1) // len(not_exists)) * (100 + t)
print(ans)
