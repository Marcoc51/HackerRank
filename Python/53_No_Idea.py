n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happy = 0
for i in range(n):
    if arr[i] in a:
        happy += 1
    elif arr[i] in b:
        happy -= 1
print(happy)
