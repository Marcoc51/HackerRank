import numpy

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
res = numpy.array(arr)
min_list = numpy.min(res, axis=1)
print(numpy.max(min_list))
