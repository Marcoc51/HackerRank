import math

AB = int(input())
BC = int(input())
angle = int(round(math.degrees(math.atan(AB / BC)), 0))
degree_sign = u'\N{DEGREE SIGN}'
print(str(angle) + degree_sign)
