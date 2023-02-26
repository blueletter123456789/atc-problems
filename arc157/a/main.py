def main():
    n, a, b, c, d = map(int, input().split())

    if abs(b - c) > 1:
        return False
    elif abs(b - c) == 1:
        return True
    elif b != 0:
        return True
    elif a == 0 or d == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Yes" if main() else "No")
