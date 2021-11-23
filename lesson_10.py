'''
Задание

У нас есть интернет магазин. Это стартап, потому до проверки ниши много действий делаются руками.
Поставщик прислал архив, в котором есть прайс и папка с картинками.
Прайс: id, name, brand, price
Картинки: имя файла начинается с id товара

Есть правило установки цены:
Для бренда Matchbox скидка от поставщика 40%
Для остальных 30%
Продажная цена = цена закупки * 2

Задача: подготовить папку для выгрузки на сайт интернет магазина

файл выгрузки: sku (=id), name, brand, price (продажная цена), image. Формат json {"key": "name"} или [{"key": "name"}]

Картинка должна лежать в папке: catalog/products

 - Создать словарь с ключами - шаблон
 - Нужно подвязать картинку
 - Функция для просчета продажной цены
 - Функция для картинки

 1) Читаем цсв файл - массив словарей
 2) Продажная цена
 3) Картинка (добавление пути и копирование)
 4) Сохраняем json

'''

import csv

# file_obj = open('names.txt', 'r')
#
# '''
# file_obj используем
# '''
#
# file_obj.close()


# with open('ls10/price.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)
#
#
# with open('ls10/price.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(dict(row))
#
# pass

# from lesson_10_price_export import read_csv_to_list_of_dicts
# import read_csv_to_list_of_dicts


import json


with open('ls10/products.json', 'r') as json_file:
    data = json.load(json_file)

print(data)