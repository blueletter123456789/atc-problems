s = input()
expected = 'atcoder'

cnt = 0
i = 0
while s != expected:
    if s[i] == expected[i]:
        i += 1
        continue
    j = i + 1
    while expected[i] != s[j]:
        j += 1
    cnt += j - i
    s = expected[:i+1] + s[i:j] + s[j+1:]

print(cnt)
