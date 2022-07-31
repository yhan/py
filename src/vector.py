from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def abs(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __mul__(self, other):
        x  = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)


v1 = Vector(2, 4)
v2 = Vector(2, 1)

mul = v1 * v2
print(mul)

print(f'hypot of {v1} = {v1.abs()}')
# print(f'hypot of {v1} = {abs(v1)}')


# # derived class
# class MultiVector(Vector):
#     def __mul__(self, other):
#         x  = self.x * other.x
#         y = self.y * other.y
#         return MultiVector(x, y)
#
# a = MultiVector(5,6)
# b = MultiVector(7,8)
#
# ab = a * b
# print(ab)

