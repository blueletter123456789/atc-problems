def main():
    a = input()
    b = input()

    if len(a) > len(b):
        return "GREATER"
    elif len(a) < len(b):
        return "LESS"

    for i, j in zip(a, b):
        if i > j:
            return "GREATER"
        elif i < j:
            return "LESS"

    return "EQUAL"


if __name__ == "__main__":
    print(main())
