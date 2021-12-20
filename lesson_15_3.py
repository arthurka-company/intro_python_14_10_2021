
class SafeRectangleWithProperty:

    def __init__(self, a, b):
        self._a = a
        self._b = b
        self.perimetr = None
        self.square = None
        self.update_params()

    def validate_sides(self, a, b):
        pass

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a
        self.update_params()

    @b.setter
    def b(self, b):
        self._b = b
        self.update_params()

    def update_params(self):
        self.validate_sides(self._a, self._b)
        self.perimetr = self.count_perimetr()
        self.square = self.count_square()

    def count_perimetr(self):
        return (self._a + self._b) * 2

    def count_square(self):
        return self._a * self._b

#
# rect = SafeRectangleWithProperty(10, 20)
# print(rect.perimetr, rect.square)
# print(rect.a, rect.b)
# rect.a = 100
# print(rect.a, rect.b)
# print(rect.perimetr, rect.square)


class Square(SafeRectangleWithProperty):

    def validate_sides(self, a, b):
        if a != b:
            raise ValueError(f'Sides must be equal: a={a}, b={b}')


rect = SafeRectangleWithProperty(10, 20)

sq = Square(10, 10)

print(sq.square, sq.perimetr)

sq.a = 20
print(sq.square, sq.perimetr, sq.validate_sides())
