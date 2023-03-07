n, k = map(int, input().split())

lst = set(input().split())
lst = sorted(list(map(int, lst)))
ans = -1
for idx, num in enumerate(lst[:k]):
    if idx != num:
        break
    ans = idx

print(ans + 1)
