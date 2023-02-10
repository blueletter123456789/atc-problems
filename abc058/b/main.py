o = input()
e = input()

ans = []
for a, b in zip(o, e):
    ans.append(a + b)

if len(o) - len(e):
    ans.append(o[-1])

print("".join(ans))
