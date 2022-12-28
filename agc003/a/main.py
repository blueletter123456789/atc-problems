s = set(input())

is_exist = True
if any(['N' in s and 'S' not in s,
        'S' in s and 'N' not in s,
        'W' in s and 'E' not in s,
        'E' in s and 'W' not in s]):
    is_exist = False

print('Yes' if is_exist else 'No')
