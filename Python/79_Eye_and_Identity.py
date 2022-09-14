import numpy

numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(numpy.eye(n, m))
