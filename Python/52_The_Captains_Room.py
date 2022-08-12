from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))
f = Counter(rooms)
for i in set(rooms):
    if f[i] == 1:
        print(i)
        break
