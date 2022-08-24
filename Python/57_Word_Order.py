from collections import Counter

words = []
for _ in range(int(input())):
    words.append(input())

word_count = Counter(words)
values = word_count.values()

print(len(set(words)))
for value in values:
    print(value, end=' ')
