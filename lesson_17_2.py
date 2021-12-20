'''
 Сколько вам лет в днях? Это легко вычислить - достаточно вычесть свой день рождения от сегодняшнего дня.
  Мы имеем реальную задачу - посчитать разницу между любыми датами.

У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например,
 19 апреля 1982 будет (1982, 4, 19). Вы должны найти разницу
 в днях между имеющимися датами. Например, между сегодня и вчера = 1 день.
 Разница между днями всегда будет положительной или нулем, не забывайте про абсолютное значение.

Входные данные: Две даты, как кортежи целых чисел.

Выходные данные: Разница между датами в днях, как целое число.
'''
import datetime



def days_diff(date_1, date_2):
    date_1 = datetime.date(year=date_1[0], month=date_1[1], day=date_1[2])
    date_2 = datetime.date(year=date_2[0], month=date_2[1], day=date_2[2])
    delta = date_2 - date_1
    return abs(delta.days)



assert days_diff((1982, 4, 19), (1982, 4, 12)) == 7


#
# print(datetime.date.today())
# print(type(datetime.date.today()))
# today = datetime.date.today()
# print(dir(today))
# print(today.year, today.month, today.day)
# print(today.replace(day=1))
# print(today.strftime('%Y-/-%m / %'))
# print(datetime.datetime.strptime('2021-12-31', '%Y-%m-%d').date())
