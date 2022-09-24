import numpy

n = int(input())
a_list = []
b_list = []
for i in range(n):
    a_list.append(list(map(int, input().split())))
for i in range(n):
    b_list.append(list(map(int, input().split())))
a = numpy.array(a_list)
b = numpy.array(b_list)
print(numpy.matmul(a, b))
# print(numpy.dot(a, b))
