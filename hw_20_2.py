"""
Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd")
и произвольное количество чисел, возвращая только те,
которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""


def filter_numbers(filter_type, *args):
    if filter_type == "even":      #если пользователь хочет чётные числа
        return [x for x in args if x % 2 == 0] #возьми x из args если x делится на 2 добавь в список
    elif filter_type == "odd":     #если нужны нечётные числа
        return [x for x in args if x % 2 != 0]  #возьми x если НЕ делится на 2 добавь
    else:
        return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))