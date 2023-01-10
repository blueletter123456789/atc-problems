expected = 'keyence'
s = input()

is_same = True if expected == s[:len(expected)] else False
for i in range(len(expected)):
    splited = s[:i] + s[-(len(expected) - i):]
    if expected == splited:
        is_same = True
        break

print('YES' if is_same else 'NO')
