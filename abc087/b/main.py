lst = sorted([
    (int(input()), 500),
    (int(input()), 100),
    (int(input()), 50),
], reverse=True)
x = int(input())

ans = 0
for i in range(lst[0][0] + 1):
    for j in range(lst[1][0] + 1):
        for k in range(lst[2][0] + 1):
            nums = (lst[0][1] * i +
                    lst[1][1] * j +
                    lst[2][1] * k)
            if x == nums:
                ans += 1

print(ans)
