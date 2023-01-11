from collections import Counter

w = Counter(input())

is_beauty = True
for num in w.values():
    if num % 2:
        is_beauty = False
        break

print('Yes' if is_beauty else 'No')
