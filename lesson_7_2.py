# Модули


import collections


# # my_dict = {}
# my_dict = collections.defaultdict(int)
# print(my_dict)
# print(my_dict['key'])
#
# text = 'John is the son of John second. Second son of John second is William second.'
# my_list = text.lower().replace('.', '').split()
# print(my_list)
# # print('f' == 'F')
# count_dict = collections.defaultdict(int)
# for word in my_list:
#     count_dict[word] += 1
#
# print(count_dict)


# text = 'John is the son of John second. Second son of John second is William second.'
# my_list = text.lower().replace('.', '').split()
# counter = collections.Counter(my_list)
# most_common = counter.most_common(3)
#
# # print(most_common)


import os

# print(dir(os))
# for name in dir(os):
#     print(name)
print(os.listdir())
print(os.path.isfile('lesson_7.py'))
print(os.path.isdir('/home/tarchanskyj/projects/personal/hillel/intro_python_14_10_2021'))
print(os.path.basename('http://domen.com//home/tarchanskyj/projects/personal/hillel/intro_python_14_10_2021/file.txt'))
