# from collections import defaultdict
# import heapq

# M = 998244353

# x = int(input())

# seen = defaultdict(int)
# seen[x] = 1
# splited = [-x]
# heapq.heapify(splited)
# while True:
#     biggest = -1 * heapq.heappop(splited)
#     a, b = biggest//2, (biggest+1)//2
#     if biggest >= a * b:
#         break
#     seen[biggest] -= 1
#     append_lst = [-a, -b]
#     for num in append_lst:
#         heapq.heappush(splited, num)
#     seen[a] += 1
#     seen[b] += 1

# ans = 1
# for key, value in seen.items():
#     ans *= (key ** value) % M
#     ans %= M

# print(ans)

M = 998244353

X = int(input())

seen = dict()


def func(x):
    if x <= 4:
        return x
    if x in seen:
        return seen[x]
    a, b = x//2, (x+1)//2
    seen[x] = (func(a) * func(b)) % M
    return seen[x]


ans = func(X)

print(ans)
