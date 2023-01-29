n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X.sort()
Y.sort()

ans = []
ans.append((abs(X[-1][0] - X[0][0]), (X[-1][1], Y[0][1])))
ans.append((abs(Y[-1][0] - Y[0][0]), (Y[-1][1], Y[0][1])))
ans.append((abs(X[-1][0] - X[1][0]), (X[-1][1], X[1][1])))
ans.append((abs(Y[-1][0] - Y[1][0]), (Y[-1][1], Y[1][1])))
ans.append((abs(X[-2][0] - X[0][0]), (X[-2][1], X[0][1])))
ans.append((abs(Y[-2][0] - Y[0][0]), (Y[-2][1], Y[0][1])))

ans.sort(reverse=True)

if ans[0][1] != ans[1][1]:
    print(ans[1][0])
else:
    print(ans[2][0])
