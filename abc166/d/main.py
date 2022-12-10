x = int(input())

seen = dict()
# "n = 120**5-119**5"で"n<=10**9"となるため−118 <= n <= 119で全探索をする
for i in range(10**5):
    seen[i**5] = i

ans_a = ans_b = -1
for j in range(10**5):
    b = j**5
    if x - b in seen:
        ans_a, ans_b = seen[x-b], -j
        break
    if x + b in seen:
        ans_a, ans_b = seen[x+b], j
        break

print(ans_a, ans_b)
