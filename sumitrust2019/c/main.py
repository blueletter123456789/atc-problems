x = int(input())

prices = [100, 101, 102, 103, 104, 105]
dp = [0] * (x+1)
dp[0] = 1

for price in prices:
    for j in range(0, x+1):
        if j < price:
            continue
        if dp[j-price]:
            dp[j] = 1


print(dp[x])
