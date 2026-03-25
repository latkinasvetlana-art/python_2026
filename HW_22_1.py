''''1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.

Данные:

orders = [

    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}

]

Пример вывода:

['Chair', 'Laptop']'''




def price_add(orders):
    result = [order["product"] for order in orders if order["price"] > 500]
    result.sort()
    return result

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
print(price_add(orders))