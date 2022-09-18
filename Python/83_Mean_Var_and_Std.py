import numpy

n, m = map(int, input().split())
arr_list = []
for _ in range(n):
    arr_list.append(list(map(int, input().split())))
arr = numpy.array(arr_list)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis=None), 11))
