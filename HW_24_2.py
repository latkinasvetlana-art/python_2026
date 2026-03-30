# Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:
# 28



def sum_nested(lst):
    total = 0  # переменная для суммы

    for x in lst:  # перебираем каждый элемент
        
        if isinstance(x, list):  
            total += sum_nested(x)  # рекурсия
        
        else:
            total += x  # просто добавляем число

    return total  # возвращаем итог


# ДАННЫЕ должны быть снаружи
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

# ВЫЗОВ функции
print(sum_nested(nested_numbers))