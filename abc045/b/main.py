from collections import deque

cards = dict()
cards['a'] = deque(input())
cards['b'] = deque(input())
cards['c'] = deque(input())

tgt = 'a'
while True:
    if not len(cards[tgt]):
        break
    tgt = deque.popleft(cards[tgt])

print(tgt.upper())
