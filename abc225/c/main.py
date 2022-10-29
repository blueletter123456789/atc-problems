def main():
    start_num = ((B[0][0]-1) // 7) * 7 + 1
    if B[0][0]-start_num + m > 7:
        print('No')
        return
    ans = True
    for i in range(n):
        for j in range(m):
            if i+1 < n and B[i][j]+7 != B[i+1][j]:
                ans = False
                break
            if j+1 < m and B[i][j]+1 != B[i][j+1]:
                ans = False
                break
        if not ans:
            break

    print('Yes' if ans else 'No')


if __name__ == '__main__':
    n, m = map(int, input().split())

    B = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        B.append(row)

    main()
