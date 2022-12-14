n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

is_exist = True

for j in range(1, n):
    for i in range(1, n):
        prev = c[i-1][j] - c[i-1][j-1]
        curr = c[i][j] - c[i][j-1]
        if prev != curr:
            is_exist = False
            break
    if not is_exist:
        break
print('Yes' if is_exist else 'No')

a = list()
b = list()
if is_exist:
    a = [str(min(row)) for row in c]
    b = [str(c[0][i]-int(a[0])) for i in range(n)]
    print(' '.join(a))
    print(' '.join(b))
