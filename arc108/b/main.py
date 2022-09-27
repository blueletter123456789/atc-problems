from collections import deque

n = int(input())
s = input()

que = deque([])
for si in s:
    que.append(si)
    
    if si != 'x':
        continue

    while len(que) >= 3:
        tmp = ''
        for _ in range(3):
            tmp = que.pop() + tmp
        if tmp != 'fox':
            for ti in tmp:
                que.append(ti)
            break

print(len(que))
