import random


# point_a = {
#     'x': random.randint(-100, 100),
#     'y': random.randint(-100, 100)
# }
# point_b = {
#     'x': random.randint(-100, 100),
#     'y': random.randint(-100, 100)
# }
# point_c = {
#     'x': random.randint(-100, 100),
#     'y': random.randint(-100, 100)
# }
# triangle = {
#     'A': point_a,
#     'B': point_b,
#     'C': point_c
# }
# print(triangle)


# def create_triangle():
#     point_a = {
#         'x': random.randint(-100, 100),
#         'y': random.randint(-100, 100)
#     }
#     point_b = {
#         'x': random.randint(-100, 100),
#         'y': random.randint(-100, 100)
#     }
#     point_c = {
#         'x': random.randint(-100, 100),
#         'y': random.randint(-100, 100)
#     }
#     triangle = {
#         'A': point_a,
#         'B': point_b,
#         'C': point_c
#     }
#     return triangle



def create_point():
    point = {
        'x': random.randint(-100, 100),
        'y': random.randint(-100, 100)
    }
    return point


def create_triangle():
    point_a = create_point()
    point_b = create_point()
    point_c = create_point()
    triangle = {
        'A': point_a,
        'B': point_b,
        'C': point_c
    }
    return triangle


A = create_triangle()
B = create_triangle()



print(A)
print(B)

a = int('45')
