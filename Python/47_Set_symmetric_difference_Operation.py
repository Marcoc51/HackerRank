n = int(input())
n_set = set(input().split())

b = int(input())
b_set = set(input().split())

res = n_set.symmetric_difference(b_set)
print(len(res))
