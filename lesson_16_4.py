

class MyClass:
    CONST = 100

    def __init__(self, arg):
        self.arg = arg

    @classmethod
    def cls_method(cls, a):
        print(cls.CONST, a)

    def do_smth(self):
        print(self.arg)

    def print_smth(self):
        print('Test')

    @staticmethod
    def sum_two_integers(a, b):
        return a + b

    @staticmethod
    def multiply_two_integers(a, b):
        return a * b

obj = MyClass(100)
# MyClass.print_smth()
obj.print_smth()
print(obj.sum_two_integers(3, 5))

print(MyClass.sum_two_integers(10, 34))

MyClass.cls_method(200)


