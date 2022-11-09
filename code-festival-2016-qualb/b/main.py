n, a, b = map(int, input().split())
s = input()

cnt = dict()
cnt['a'] = cnt['b'] = cnt['c'] = 0
for i in s:
    flg = True

    if i == 'c':
        flg = False
    elif cnt['a']+cnt['b'] >= a+b:
        flg = False
    elif i == 'b' and cnt['b'] >= b:
        flg = False

    if flg:
        print('Yes')
        cnt[i] += 1
    else:
        print('No')
