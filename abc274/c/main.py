n = int(input())
a = list(map(int, input().split()))

ans = [0]*(n*2+2)
for i, num in enumerate(a):
    ans[(i+1)*2] = ans[num] + 1
    ans[(i+1)*2+1] = ans[num] + 1

for i in range(1, n*2+2):
    print(ans[i])
