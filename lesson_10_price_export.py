import csv
import copy
import os
import shutil
import json


DEFAULT_DISCOUNT = 0.3
INPUT_IMAGE_FOLDER = 'ls10/images'


def read_csv_to_list_of_dicts(file_path, delimiter=','):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        data = [dict(row) for row in reader]
    return data


def get_product_sell_price(product, brand_discount):
    if product['brand'] in brand_discount.keys():
        price = float(product['price']) * (1 - brand_discount[product['brand']]) * 2
    else:
        price = float(product['price']) * (1 - DEFAULT_DISCOUNT) * 2
    return price


# def update_products_with_sell_price(data_array, brand_discount=None):
#     if brand_discount is None:
#         brand_discount = {}
#     result = copy.deepcopy(data_array)
#     for product in result:
#         product['price'] = get_product_sell_price(product, brand_discount)
#     return result


# def get_image_path(product):
#     files = os.listdir(INPUT_IMAGE_FOLDER)
#     print(files)
#     for name in files:
#         if name.
#     return ''


def read_images(folder):
    files = os.listdir(folder)
    result = {}
    for name in files:
        if '_' in name:
            file_name = name.split('_')[0]
        elif '|' in name:
            file_name = name.split('|')[0]
        else:
            file_name = name.split('.')[0]
        result[file_name] = f'catalog/products/{name}'
    return result


def update_products_with_extra_data(data_array, image_data, brand_discount=None):
    if brand_discount is None:
        brand_discount = {}
    result = copy.deepcopy(data_array)
    for product in result:
        product['price'] = get_product_sell_price(product, brand_discount)
        product['image'] = image_data.get(product['id'])
    return result


def copy_images(products):
    for product in products:
        image_name = os.path.basename(product['image'])
        shutil.copy(
            f'{os.getcwd()}/ls10/images/{image_name}',
            f'{os.getcwd()}/ls10/{product["image"]}'
        )


def save_data_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    price_file_path = 'ls10/price.csv'
    brand_discount = {
        'Matchbox': 0.4,
        'Chico': 0.1
    }
    image_data = read_images(INPUT_IMAGE_FOLDER)
    print(image_data)
    data = read_csv_to_list_of_dicts(price_file_path)
    # print(data)
    # data = update_products_with_sell_price(data, brand_discount=brand_discount)
    data = update_products_with_extra_data(data, image_data, brand_discount=brand_discount)
    print(data)
    copy_images(data)
    save_data_to_json('ls10/products.json', data)




