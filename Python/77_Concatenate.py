import numpy

n, m, p = input().split()

arr1 = []
for i in range(int(n)):
    arr1.append(list(map(int, input().split())))

arr2 = []
for i in range(int(m)):
    arr2.append(list(map(int, input().split())))

print(numpy.concatenate((numpy.array(arr1), numpy.array(arr2)), axis=0))
