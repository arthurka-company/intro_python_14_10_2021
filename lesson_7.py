# Словари, методы словарей.

# *** Создание
# my_dict = {'test': 'test', 'key': 'rf'}
# print(my_dict)

# my_dict = dict.fromkeys([1, 2, 3], 0)
# print(my_dict)

my_dict = {i: str(i) for i in range(10) if i > 3}
my_dict['nested_key'] = {'key': 'value'}

# print(list(my_dict))

my_dict = {4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 'nested_key': {'key': 'value'}}
# Создание ***

# *** Чтение по ключу
# result = my_dict.get('nested_key', {}).get('key9', {}).get('key', '33')
# for item in result:
#     print(item)
# Чтение по ключу ***


# *** keys, items, values
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# print(my_dict.values())
# for key in my_dict.values():
#     print(key)

# a, b = (12, 34)
# print(a)
# print(b)

# [(4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), ('nested_key', {'key': 'value'})]
# print(list(my_dict.items()))
# print(type(my_dict.items()))
# for key, value in my_dict.items():
#     print(key, value)

# dict([(), ()])

# print(my_dict.pop('nested_keye', None))

# print(my_dict)
# print(my_dict.popitem())
# print(my_dict.popitem())
# print(my_dict)

# print(my_dict)
# my_dict.update({43: 100})
# print(my_dict)


# Найти топ 3 слова в тексте.
text = 'John is the son of John second. Second son of John second is William second.'
my_list = text.lower().replace('.', '').split()
print(my_list)
# print('f' == 'F')
count_dict = {}
for word in my_list:
    if word in count_dict.keys():
        count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)

# [('4', 4), ('5', 5)]
result = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:3]
# print(sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:3])

# item = (1, 2)
# print(item[1])
