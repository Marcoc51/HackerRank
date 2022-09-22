import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a, b))
print(numpy.outer(a, b))
