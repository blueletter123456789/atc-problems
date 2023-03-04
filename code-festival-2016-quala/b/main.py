n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))
cnt = 0
seen = [False] * n

for i, j in enumerate(a):
    if not seen[j] and a[j] == i:
        cnt += 1
        seen[i] = True

print(cnt)
