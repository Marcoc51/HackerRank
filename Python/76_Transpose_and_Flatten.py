import numpy

n, m = input().split()
arr = []
for i in range(int(n)):
    arr.append(list(map(int, input().split())))
res = numpy.array(arr)
print(numpy.transpose(res))
print(res.flatten())
