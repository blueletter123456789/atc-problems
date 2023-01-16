n = int(input())
a = list(map(int, input().split()))

ans = 0
for num in a:
    ans += num - 1

print(ans)
