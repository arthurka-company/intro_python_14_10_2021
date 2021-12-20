# Полиморфизм. Декораторы



# def decorator_func(func):
#     print('In decorator')
#     print(type(func))
#     return func

#
# def decorator_func(func):
#     print('In decorator')
#     def wrapper():
#         print('Before func run')
#         func()
#         print('After func run')
#     return wrapper
#
#
# @decorator_func
# def my_func():
#     print('My func')
#
#
# if __name__ == '__main__':
#     # a = my_func
#     # print(type(a))
#     print('run')
#     # a()
#     my_func()
#     # my_func()

import time


def time_decorator(func):
    def wrapper(number):
        start_time = time.time()
        res = func(number)
        print('Time:', time.time() - start_time)
        return res
    return wrapper


@time_decorator
def factor(number):
    res = 1
    for i in range(1, number):
        res *= i
    return res


if __name__ == '__main__':
    start_time = time.time()
    # res = factor(100000)
    # print(res)
    # res = factor(200)
    # print('Time:', time.time() - start_time)
    # print(res)

    for i in [5, 50, 500, 5000, 50000]:
        factor(i)
