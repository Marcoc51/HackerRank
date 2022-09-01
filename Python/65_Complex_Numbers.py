import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        a = self.real + no.real
        b = self.imaginary + no.imaginary
        res = Complex(a, b)
        return res
        
    def __sub__(self, no):
        a = self.real - no.real
        b = self.imaginary - no.imaginary
        res = Complex(a, b)
        return res
        
    def __mul__(self, no):
        a = (self.real * no.real) - (self.imaginary * no.imaginary)
        b = (self.real * no.imaginary) + (self.imaginary * no.real)
        res = Complex(a, b)
        return res

    def __truediv__(self, no):
        result = complex(self.real, self.imaginary) / complex(no.real, no.imaginary)
        res = Complex(result.real, result.imag)
        return res

    def mod(self):
        result = math.sqrt((self.real ** 2) + (self.imaginary **2))
        res = Complex(result, 0)
        return res
