import random


MAX_LIMIT = 10
MIN_LIMIT = -10


def create_point():
    # global MAX_LIMIT
    # MAX_LIMIT = 100
    point = {
        'x': random.randint(MIN_LIMIT, MAX_LIMIT),
        'y': random.randint(MIN_LIMIT, MAX_LIMIT)
    }
    return point

#
# def create_triangle(name):
#     assert isinstance(name, str)
#     assert len(name) == 3
#     point_names = list(name)
#     point_a = create_point()
#     point_b = create_point()
#     point_c = create_point()
#     triangle = {
#         'A': point_a,
#         'B': point_b,
#         'C': point_c
#     }
#     return triangle


def create_triangle(name):
    assert isinstance(name, str)
    assert name.isalpha()
    assert len(name) == 3
    point_names = list(name)
    triangle = {}
    for point_name in point_names:
        triangle[point_name] = create_point()
    return triangle


A = create_triangle('ABC')
B = create_triangle('KLM')

print(A)
print(B)
# print(MAX_LIMIT)

# assert 3 == 3
