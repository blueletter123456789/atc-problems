def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def main(left, right):
    max_num = 0
    max_idx = min(1500, right - left)

    for i in range(max_idx):
        tmp_l, tmp_r = left, right - i
        while gcd(tmp_r, tmp_l) != 1:
            tmp_l += 1
        max_num = max(max_num, tmp_r - tmp_l)
    return max_num


if __name__ == "__main__":
    left, right = map(int, input().split())
    print(main(left, right))
