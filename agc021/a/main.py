n = input()
len_n = len(n)

ans = (len_n-1)*9 + int(n) // (10**(len_n-1))
if n[1:].count('9') != len_n-1:
    ans -= 1

print(ans)
