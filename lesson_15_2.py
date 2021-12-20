# __str__
# __repr__

# __init__
# __new__
# from lesson_15 import SafeRectangleWithProperty
#
#
# class Single(SafeRectangleWithProperty):
#     # obj = None
#     #
#     # def __new__(cls, *args, **kwargs):
#     #     if cls.obj is None:
#     #         cls.obj = object.__new__(cls, *args, **kwargs)
#     #     return 3
#     #
#     def __init__(self):
#         print('init')
#         # self.__update_params()
#
#
# s = Single()
# s._count_perimetr()


# class Single(SafeRectangleWithProperty):
# class Single(object):
#     obj = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.obj is None:
#             print('new')
#             # cls.obj = object.__new__(cls, *args, **kwargs)
#             cls.obj = super().__new__(cls, *args, **kwargs)
#         return cls.obj
#
#
# s_1 = Single()
# s_1.attr = 100
# print(s_1.attr)
# s_2 = Single()
# print(s_2.attr)

class Parent:
    def new_method(self):
        print('Parent')


class Child(Parent):
    # pass
    def new_method(self):
        super().new_method()
        print('Child')


ch = Child()
ch.new_method()


class ListView:
    model = None

    def get_queryset(self):
        data = self.model.get_data()
        return data


class PersonListView(ListView):
    model = Person

    def get_queryset(self):
        data = super().get_queryset()
        # data filtering
        data = data.filter(age>20)
        return data

    def unique_method(self):
        pass
