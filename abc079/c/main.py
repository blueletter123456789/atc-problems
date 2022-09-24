s = [int(i) for i in input()]

pat = ''
for i in range(1 << 3):
    cnt = s[0]
    pat = list()
    for j in range(3):
        if i & (1 << j):
            cnt += s[j+1]
            pat.append('+')
        else:
            cnt -= s[j+1]
            pat.append('-')
    if cnt == 7:
        break

ans = ''
for i in range(len(pat)):
    ans += str(s[i]) + pat[i]

ans += str(s[-1]) + '=7'
print(ans)
