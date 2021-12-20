'''
Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
backward_string_by_word('hello   world and you') == 'olleh   dlrow'
'''


# def backward_string_by_word(text):
#     result = ''
#     # result = text[::-1]
#     result = text.split(' ')
#     print(result)
#     result = [i[::-1] for i in result]
#     result = ' '.join(result)
#     return result
#
# print(backward_string_by_word('hello   world and you'))


'''

Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в первом аргументе, а сами данные 
по товарам будут переданы вторым аргументом.

Вх. данные: Число и список словарей (int and list of dicts). Каждый словарь имеет 2 ключа "name" и "price".
Вых. данные: Такой же как и второй аргумент.


bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]

'''


def bigger_price(number, data):
    result = sorted(data, key=lambda item: item['price'], reverse=True)
    return result[:number]


# # [[[], []], [[], []]]
#
# print(bigger_price(3, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]))
#
# word = 'asdfghjklzxcvbnm'
#
# print(word[3::1])
# print(word[3:5:1])
# print(word[3:5:-1])
#
# # print(word[:-1])
# print(word[-1])



MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(text):
    result = []
    words = text.split('   ')
    for word in words:
        letters = word.split(' ')
        decoded_word = [MORSE[i] for i in letters]
        decoded_word = ''.join(decoded_word)
        result.append(decoded_word)
        # print(letters)

    print(words)
    print(result)
    result = ' '.join(result)
    print(result)
    return result



morse_decoder("... --- -- .   - . -..- -")
morse_decoder("..--- ----- .---- ---..")
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")

