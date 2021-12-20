# Полиморфизм. Декораторы


# print(3 + 4)
#
# print('3' + '4')
#
# print([3] + [4, 5])

# object
#
# list
#
# dict

int

# float(234)


class MyDict(dict):

    def __add__(self, value, *args, **kwargs):  # real signature unknown
        """ Return self+value. """
        print(value, '0')
        print(args, '1')
        print(kwargs, '2')
        self.update(value)
        return self



dict_1 = MyDict(key=5)
dict_2 = MyDict(key_2=10)
print(dict_1, dict_2)

print(dict_1 + dict_2, 'result')
# float(dict_1)


# 20:26




# print({'key': 'v'} + {'key2': 'v2'})



