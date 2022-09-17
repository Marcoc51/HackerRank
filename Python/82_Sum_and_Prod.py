import numpy

n, m = map(int, input().split())
arr_list = []
for _ in range(n):
    arr_list.append(list(map(int, input().split())))
arr = numpy.array(arr_list)
print(numpy.prod(numpy.sum(arr, axis=0)))
