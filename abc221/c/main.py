n = input()
n = sorted(list(n), reverse=True)

max_num = 0
for i in range(1, 1 << len(n)-1):
    x, y = '', ''
    for j in range(len(n)):
        if i & (1 << j):
            x += n[j]
        else:
            y += n[j]
    
    max_num = max(max_num, int(x)*int(y))

print(max_num)
