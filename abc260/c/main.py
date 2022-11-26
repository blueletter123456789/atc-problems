def main():
    n, x, y = map(int, input().split())

    stones = [[0]*2 for _ in range(n+1)]
    stones[n][0] = 1
    for i in range(n-1):
        stones[n-i-1][0] += stones[n-i][0]
        stones[n-i][1] += stones[n-i][0]*x
        stones[n-i-1][0] += stones[n-i][1]
        stones[n-i-1][1] += stones[n-i][1]*y

    print(stones[1][1])


if __name__ == '__main__':
    main()
