'''

https://jsonplaceholder.typicode.com/
Скачать фото через REST API. Фото сохранять в папки по альбомам.
На вход нужно передавать количество альбомов, которые хотим скачать.
'''

import requests
import os

# requests.get()  !!!
# requests.post()

# requests.patch()
# requests.put()
# requests.delete()

ALBUM_URL = 'https://jsonplaceholder.typicode.com/albums'
PHOTO_URL = 'https://jsonplaceholder.typicode.com/photos'


def get_albums(number):
    # Функция для получения списка альбомов в формате json
    response = requests.get(ALBUM_URL)
    # print(response.json())
    albums_data = response.json()  # Преобразование ответа в json
    # albums_data = albums_data[:number]
    return albums_data[:number]  # слайс для того, чтобы отдать массив с нужным количеством альбомов


def get_photos_by_album_id(album_id, number=5):
    # запрос на получение массива фотографий отправляется с фильтрацией по нужному альбому
    response = requests.get(
        f'{PHOTO_URL}?albumId={album_id}'
    )
    data = response.json()
    return data[:number]


def save_photos_for_album(folder_name, data):
    # Сохранение фото в папку.
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
    for photo in data:
        # Фото скачиваем через запрос
        image_response = requests.get(photo['url'])
        with open(f'{folder_name}/{photo["title"]}.jpg', 'wb') as f:
            f.write(image_response.content)


if __name__ == '__main__':
    # Сначала получим массив альбомов, которые нужно скачать
    albums = get_albums(2)
    print(albums)
    # Проверка существует ли папка, в которую сохранить результат, если папки нет, то она будет создана
    if not os.path.isdir('photos'):
        os.makedirs('photos')

    for album in albums:
        # Проходимся по массиву альбомов и скачиваем массив фотографий альбома
        photos = get_photos_by_album_id(album['id'])
        print(photos)

        save_photos_for_album(f"photos/{album['title']}", photos)

