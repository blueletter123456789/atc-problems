x = {char: idx for idx, char in enumerate(input())}

n = int(input())
lst = []
for _ in range(n):
    s = input()
    cnt = []
    for char in s:
        cnt.append(x[char])
    lst.append((cnt, s))

for name in sorted(lst):
    print(name[1])
