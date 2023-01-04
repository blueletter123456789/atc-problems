s = input()
k = int(input())

for num in s[:k]:
    if num != '1':
        break

print(num)
