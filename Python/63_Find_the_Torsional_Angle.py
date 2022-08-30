import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        result = Points(x, y, z)
        return result

    def dot(self, no):
        res = (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
        return res

    def cross(self, no):
        x = (self.y * no.z) - (self.z * no.y)
        y = (self.z * no.x) - (self.x * no.z)
        z = (self.x * no.y) - (self.y * no.x)
        return Points(x, y, z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
