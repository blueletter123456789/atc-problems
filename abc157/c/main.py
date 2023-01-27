def main():
    n, m = map(int, input().split())

    lst = [-1] * n
    for _ in range(m):
        s, c = map(int, input().split())
        if lst[s-1] >= 0 and lst[s-1] != c:
            return -1
        lst[s-1] = c

    if n == 1:
        return max(lst[0], 0)

    ans = 0
    for i, k in enumerate(lst):
        if i == 0 and k == 0:
            return -1
        if i == 0 and k < 0:
            ans += 1
        elif k < 0:
            ans *= 10
        else:
            ans *= 10
            ans += k
    return ans


if __name__ == '__main__':
    print(main())
