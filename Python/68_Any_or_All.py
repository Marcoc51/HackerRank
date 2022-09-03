n = int(input())
nums = list(map(int, input().split()))
print(any([str(i) == str(i)[::-1] for i in nums]) and all([i > 0 for i in nums]))
