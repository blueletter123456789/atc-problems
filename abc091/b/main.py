from collections import defaultdict

n = int(input())
blue_words = defaultdict(int)
for _ in range(n):
    word = input()
    blue_words[word] += 1

m = int(input())
red_words = defaultdict(int)
for _ in range(m):
    word = input()
    red_words[word] += 1

ans = 0
for word, count in blue_words.items():
    ans = max(ans, count - red_words.get(word, 0))

print(ans)
