n, li = map(int, input().split())
a = list(map(int, input().split()))

ans = True
full = 0
for idx, num in enumerate(a):
    if num == 2:
        if li - full < 2:
            ans = False
            break
    full += (num + 1)

print('Yes' if ans else 'No')
