# l = [1, 23, 5, 66, 5654]
# value = 66
#
# for item in l:
#     if value == item:
#         print(item, 'Ok')
#         break


# Бульбашка
import random


def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array



N = 10
data = [random.randint(1, 100) for _ in range(N)]

print(data)
print(bubble(data))


y = O(f(n))