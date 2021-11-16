# import os
# import random
# import string
#
#
# def test_func():
#     return ''
#
#
# def test_func2():
#     return ''
#
#
# def test_func3():
#     print('pp')
#     return ''
#
# print('Ok')


# Получить координаты точек треугольника (Создать треугольник)

# point_a = {
#     'x': 0,
#     'y': 0
# }
# point_b = {
#     'x': 10,
#     'y': 10
# }
# point_c = {
#     'x': 10,
#     'y': 0
# }
# triangle = {
#     'A': point_a,
#     'B': point_b,
#     'C': point_c
# }
# print(triangle)
#
# import random

# for name in dir(random):
#     print(name)

# print(random.choice([1, 4, 5, 45, 23, 4]))
# print(random.randint(-100, 200))
# print(random.sample([1, 2, 3, 4, 5, 5, 6, 7, 8], k=5))

# value = random.randint(0, 100)
# print(value)
# if value < 30:
#     print('Ok')
# else:
#     print('No')


import random


point_a = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
point_b = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
point_c = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
triangle = {
    'A': point_a,
    'B': point_b,
    'C': point_c
}
print(triangle)

point_a1 = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
point_b1 = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
point_c1 = {
    'x': random.randint(-100, 100),
    'y': random.randint(-100, 100)
}
triangle1 = {
    'A': point_a1,
    'B': point_b1,
    'C': point_c1
}
print(triangle1)

