s = input()
n = len(s)

for i in range(1, n):
    if i % 2:
        continue
    l = s[:(n-i)//2]
    r = s[(n-i)//2:n-i]
    if l == r:
        break

print(n-i)
