import numpy

arr = list(map(float, input().split()))
print(numpy.polyval(arr, int(input())))
