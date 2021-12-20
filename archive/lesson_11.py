
# ages = [3, 4]
# result = sum(ages) / len(ages) if len(ages) > 0 else None
#
# print(result)


import requests

# for name in dir(requests):
#     print(name)

# requests.get() # забирает информацию по ссылке
# requests.post() # создание нового объекта или какое то действие на сервере
# requests.put() # обновление всего объекта
# requests.patch() # обновление только какого-то конкретного поля или полей
# requests.delete() # удаление объекта
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts/')
# # print(response.text)
# print(response.json())
#
# data = response.json()
#
# response_2 = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=2')
# # response_2 = requests.get('https://jsonplaceholder.typicode.com/posts/?title__icontains=eu')
# data_filtered = response_2.json()
# print(type(data))
# print(len(data))
# print(len(data_filtered))
# print(data_filtered)

d = [
    {
        'userId': 1,
        'id': 4,
        'title': 'eum et est occaecati',
        'body': 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit'
    }
]

# single_obj = requests.get('https://jsonplaceholder.typicode.com/posts/20/')
# patch_response = requests.patch('https://jsonplaceholder.typicode.com/posts/20/', data={'title': 'new title 2'})
#
# # print(single_obj.json())
# print(patch_response.json())
# print(patch_response.status_code)

#
# response_create = requests.post(
#     'https://jsonplaceholder.typicode.com/posts/',
#     data={
#         'title': 'our title',
#         'body': 'body'
#     }
# )
# print(response_create.status_code)
# print(response_create.json())
# new_obj = response_create.json()
#
# # r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_obj["id"]}')
# r = requests.get(f'https://jsonplaceholder.typicode.com/posts/23')
# print(r.json())


# response = requests.get('https://jsonplaceholder.typicode.com/guide/', headers={})
response = requests.get('https://jsonplaceholder.typicode.com/guide/')
print(response.status_code)
print(response.text)

# python beautifulsoup