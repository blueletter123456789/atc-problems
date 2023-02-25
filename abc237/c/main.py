def main():
    s = input()

    i, j = 0, len(s) - 1
    for char in s:
        if char == "a":
            i += 1
        else:
            break

    for char in reversed(s):
        if char == "a":
            j -= 1
        else:
            break

    if i > (len(s) - j - 1):
        return "No"

    while i < j:
        if s[i] != s[j]:
            return "No"
        i += 1
        j -= 1

    return "Yes"


if __name__ == "__main__":
    print(main())
