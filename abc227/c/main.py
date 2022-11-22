# import math

# n = int(input())

# max_a = int(n ** (1/3)) + 1
# max_b = int(math.sqrt(n)) + 1
# cnt = 0
# for a in range(1, max_a):
#     for b in range(a, min(n//a, max_b)):
#         c = n // (a * b)
#         if c < b:
#             continue
#         cnt += c - b + 1

# print(cnt)

import math


def main(n):
    cnt = 0
    for a in range(1, math.ceil(math.pow(n, 1/3))+1):
        # 最大値を計算する際はn/aの値の平方根とする必要がある
        for b in range(a, math.ceil(math.pow(n/a, 1/2))+1):
            c = int(n / (a*b))
            if a <= b <= c:
                cnt += c+1-b
            else:
                break
    print(cnt)


if __name__ == '__main__':
    n = int(input())
    main(n)
