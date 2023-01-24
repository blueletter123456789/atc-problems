x = int(input())

ans = 0
for i in range(2, 11):
    j = 1
    while True:
        k = j ** i
        if k > x:
            break
        ans = max(ans, k)
        j += 1

print(ans)
