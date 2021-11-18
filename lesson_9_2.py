import os


# print(os.getcwd())
# print(os.listdir())
# os.mkdir('test_dir')
# os.makedirs('tree_dir/included_dir')
# os.remove('test.txt')

# import shutil

# shutil.rmtree('test_dir')
# shutil.rmtree('tree_dir')

# file_path = 'tree_dir/included_dir/file.txt'

# print(os.path.basename(file_path))
# print(os.path.dirname(file_path))
# print(os.path.isfile(file_path))
# print(os.path.isdir(file_path))
# print(os.path.splitext(file_path))
# print(os.path.splitext(file_path)[1])
# basename = os.path.basename(file_path)
# print(basename)
# print(os.path.splitext(basename))


# Функция для создания папки

# def create_dir(dir_path):
#     try:
#         print('In try')
#         number = 100 / 0
#         os.mkdir(dir_path)
#         print('Finish try')
#     except ZeroDivisionError:
#         print('Error')
#     except FileExistsError:
#         print('Dir error')
#
#
# create_dir('test_dir')


# def create_dir_2(dir_path):
#     if not os.path.isdir(dir_path):
#         os.mkdir(dir_path)
#     else:
#         print('Dir exists')
#
#
# create_dir_2('test_dir')

# os.removedirs('test_dir')

# def foo(name, number=4, number_2=34):
#     print(name, number, number_2)


# foo(name='test', number=10)
# foo('test', number=10)
# foo('test', number_2=10)


# print(os.path.join('folder_1', 'folder_2/fold', 'file_name.txt'))
# print(os.path.join('folder_1/', 'folder_2/fold/', 'file_name.txt'))


# Функция, которая возвращает список файлов в папке. Файлы могут быть только названия или полные пути


def get_files_from_dir(base_dir: str, full_path: bool = True) -> list:
    if not os.path.isdir(base_dir):
        print('No such dir')
        return []
    list_dir = os.listdir(base_dir)
    result = []
    for file_name in list_dir:
        if full_path:
            result.append(os.path.join(base_dir, file_name))
        else:
            result.append(file_name)
    return result

# var name: char
# name


print(get_files_from_dir('/home/tarchanskyj/projects/personal/hillel/intro_python_14_10_2021'))


for file_name in get_files_from_dir('/home/tarchanskyj/projects/personal/hillel/intro_python_14_10_2021', full_path=False):
    print(file_name)

20:58