def main():
    diff_cnt = 0
    for a, b in zip(s, u):
        if a != b:
            diff_cnt += 1

    if diff_cnt % 2:
        print(-1)
        return

    ans = ['0']*n
    s_cnt = u_cnt = 0
    for i, (a, b) in enumerate(zip(s, u)):
        if a == b:
            continue
        if a == '1' and s_cnt < diff_cnt//2:
            s_cnt += 1
        elif b == '1' and u_cnt < diff_cnt//2:
            u_cnt += 1
        else:
            ans[i] = '1'

    print(''.join(ans))


if __name__ == '__main__':
    n = int(input())

    s, u = input(), input()

    main()
