from collections import Counter


def main():
    s = input()
    if s[0] != 'A':
        return False

    cnt = Counter(s[2:-1])
    if cnt['C'] != 1:
        return False

    for char in s:
        if char in {'A', 'C'}:
            continue
        if char != char.lower():
            return False

    return True


if __name__ == '__main__':
    print('AC' if main() else 'WA')
