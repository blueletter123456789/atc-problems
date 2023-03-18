def main():
    x, y = map(int, input().split())
    if x >= y and x % y == 0:
        return -1
    return x


if __name__ == "__main__":
    print(main())
