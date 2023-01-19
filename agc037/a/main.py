s = input()

past = ''
another = []
cnt = 0
for char in s:
    another.append(char)
    if ''.join(another) != past:
        past = ''.join(another)
        cnt += 1
        another = []

print(cnt)
