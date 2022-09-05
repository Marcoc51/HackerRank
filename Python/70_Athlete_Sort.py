n, m = input().split()
arr = []
for _ in range(int(n)):
  arr.append(list(map(int, input().rstrip().split())))
k = int(input())
arr.sort(key = lambda item:item[k])
for i in arr:
  print(*i)
