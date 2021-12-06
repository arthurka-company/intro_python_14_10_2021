# Введение в объектно ориентированное программирование

# класс
# атрибут класса
# экземпляр класса
# атрибут экземпляра класса  <-----
# метод экземпляра класса



# int()
# str()
#
# name = 'Name'
# name_2 = 'Name e'
#
# print(type(name))
#
# for i in dir(''):
#     print(i)


# class Person:
#     pass
#
#
# p = Person()
# print(dir(p))
#
# p.name = 'Name'
# p.age = 34
#
# print(type(p))
# print(p.name, p.age)



# class Person:
#     name = ''
#     age = ''
#
#
# p = Person()
# print(dir(p))
# p.age = 50
# print(p.age, p.name, p)


number = int('45')


class Rectangle:
    a = 3
    b = 3

    def __init__(self, a, b):
        print('Init')
        self.a = a
        self.b = b
        self.perimetr = self.count_perimetr()
        self.square = self.count_square()

    def count_perimetr(self):
        print('Perimetr')
        return (self.a + self.b) * 2

    def count_square(self):
        print('Square')
        return self.a * self.b
        # return Rectangle.a * Rectangle.b

    def __str__(self):
        print('STR')
        return f'Rectangle: {self.a} x {self.b}'

    def __repr__(self):
        print('Repr')
        return f'Class Rectangle, {self.a}, {self.b}'


# print(dir(Rectangle))
rect = Rectangle(10, 60)
rect.a = 100
print(rect)
print(repr(rect))
# print('None')
# print(rect.a, rect.b)
# print(dir(rect))
# print(rect.perimetr)
# print(rect.perimetr)
# print(rect.perimetr)
# print(rect.count_square())
# print(rect.count_square())
# print(rect.count_square())
# print(rect.count_square())
# print(rect.)


# import requests
#
#
# class Reader:
#     URL = 'google.com'
#
#     def __init__(self, token):
#         self.session = requests.Session()
#         self.session.headers.update(
#             {'Authorization': f'Token {token}'}
#         )
#
#
# reader = Reader('00000000000')
#


