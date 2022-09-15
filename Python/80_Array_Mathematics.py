import numpy

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a_arr = numpy.array(a)

b = []
for i in range(n):
    b.append(list(map(int, input().split())))
b_arr = numpy.array(b)

print(a_arr + b_arr)
print(a_arr - b_arr)
print(a_arr * b_arr)
print(a_arr // b_arr)
print(a_arr % b_arr)
print(a_arr ** b_arr)
