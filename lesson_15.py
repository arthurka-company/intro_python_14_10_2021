# Область видимости атрибутов и методов класса.
# Наследование классов

# __str__
# __repr__

# __init__

# Публичные - public
# без подчеркиваний в названии: <name>

# Защищенные - protected
# Название начинается с 1 подчеркивания: _<name>

# Приватные - private
# Название начинается с 2 подчеркиваний: __<name>


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._test = 100
        self.__test = 100
        self.perimetr = self.__count_perimetr()
        self.square = self.count_square()

    def __count_perimetr(self):
        self._test = 200
        self.__test = 200
        print(self._test)
        print(self.__test)
        return (self.a + self.b) * 2

    def count_square(self):
        return self.a * self.b
        # return Rectangle.a * Rectangle.b

    def __str__(self):
        return f'Rectangle: {self.a} x {self.b}'

    def __repr__(self):
        return f'Class Rectangle, {self.a}, {self.b}'


# print(dir(Rectangle))
# rect = Rectangle(10, 60)
# rect.a = 100
# print(rect._test)
# print(rect.__test)


#
# class SafeRectangle:
#
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#         self.perimetr = self.__count_perimetr()
#         self.square = self.__count_square()
#
#     def get_sides(self):
#         return [self.__a, self.__b]
#
    # def set_sides(self, a, b):
    #     self.__a = a
    #     self.__b = b
    #     self.perimetr = self.__count_perimetr()
    #     self.square = self.__count_square()
#
#     def __count_perimetr(self):
#         return (self.__a + self.__b) * 2
#
#     def __count_square(self):
#         return self.__a * self.__b
#
#
# rect = SafeRectangle(10, 20)
# print(rect.perimetr, rect.square)
# # rect.__a = 100
# print(rect.get_sides())
# rect.set_sides(100, 200)
# print(rect.perimetr, rect.square)
# print(rect.get_sides())
#
# # rect.attr = 'new'
# # print(rect.attr)


class SafeRectangleWithProperty:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__update_params()

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @a.setter
    def a(self, a):
        self.__a = a
        self.__update_params()

    @b.setter
    def b(self, b):
        self.__b = b
        self.__update_params()

    def __update_params(self):
        self.perimetr = self.__count_perimetr()
        self.square = self.__count_square()

    def _count_perimetr(self):
        return (self.__a + self.__b) * 2

    def __count_square(self):
        return self.__a * self.__b

#
# rect = SafeRectangleWithProperty(10, 20)
# print(rect.perimetr, rect.square)
# print(rect.a, rect.b)
# rect.a = 100
# print(rect.a, rect.b)
# print(rect.perimetr, rect.square)


class Square(SafeRectangleWithProperty):
    def __init__(self, a, b):
        self.__validate_sides(a, b)
        self.__a = a
        self.__b = b
        self.perimetr = self._count_perimetr()
        self.square = self.__count_square()

    def __validate_sides(self, a, b):
        if a != b:
            raise ValueError('Sides must be equal')


# rect = SafeRectangleWithProperty(10, 20)

sq = Square(10, 10)


