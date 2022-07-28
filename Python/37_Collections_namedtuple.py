from collections import namedtuple

nums = int(input())
student = namedtuple('student', input())
students = []
total = 0
for i in range(nums):
    inputs = input().split()
    students.append(student(inputs[0], inputs[1], inputs[2], inputs[3]))
    total += int(students[i].MARKS)
print('%.2f' % (total / nums))
