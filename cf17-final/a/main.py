from collections import deque

expected = 'AKIHABARA'

s = input()
que = deque([])
idx = 0
for char in expected:
    if idx < len(s) and char == s[idx]:
        que.append(s[idx])
        idx += 1
    elif char == 'A':
        que.append('A')

while idx < len(s):
    que.append(s[idx])
    idx += 1

print('YES' if ''.join(que) == expected else 'NO')
