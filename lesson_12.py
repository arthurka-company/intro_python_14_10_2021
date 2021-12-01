# import csv
#
# data = [
#     {'name': 'name', 'price': 100, 'test': 45},
#     {'name': 'name_2', 'price': 1002},
#     {'name': 'name_3', 'price': 103},
#     {'name': 'name_33', 'price': 500},
# ]
#
# headers = []
# for item in data:
#     headers += list(item.keys())
# headers = list(set(headers))
#
# # with open('out.txt', 'w') as out_f:
# #     # out_f.writelines(data)
# #     data_to_write = [f'{i["name"]} - {i["price"]}\n' for i in data]
# #     out_f.writelines(data_to_write)
#
# #
# # with open('out.csv', 'w') as out_f:
# #     writer = csv.writer(out_f)
# #     for row in data:
# #         writer.writerow([row['name'], row['price']])
#
# with open('out.csv', 'w') as out_f:
#     writer = csv.DictWriter(out_f, fieldnames=headers)
#     # writer = csv.DictWriter(out_f, fieldnames=['name', 'price'])
#     # writer = csv.DictWriter(out_f, fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     writer.writerows(data)
#     # for row in data:
#     #     writer.writerow(row)
#
#
# with open('out.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     data_out = [dict(row) for row in reader]
#
# print(data_out)



data = ['Hello', 'text', 'data', '', '45', 'TARAS']

# data = row.split()

# for item in data:
#     # if len(item) > 0:
#     #     if item[0] == 't':
#     #         print(item)
#     # if item.lower().startswith('t'):
#     #     print(item)
#     if item.startswith('t') or item.startswith('T'):
#         print(item)

a = 18
# if a > 10 and a < 50:
if 10 < a < 50:
    print(a)

