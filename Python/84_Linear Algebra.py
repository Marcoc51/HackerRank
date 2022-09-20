import numpy

arr_list = []
for _ in range(int(input())):
    arr_list.append(list(map(float, input().split())))
print(round(numpy.linalg.det(numpy.array(arr_list)), 2))
