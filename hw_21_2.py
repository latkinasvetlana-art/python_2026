"""
Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"),
("class1", "Charlie"), ("class3", "Daisy")]

Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
"""

from collections import defaultdict   #defaultdict — это особый словарь, 
#который сам создаёт пустое значение.


def group_students(students):
    groups = defaultdict(list) #если ключа нет → автоматически создаётся пустой список []
    for cls, name in students:
        groups[cls].append(name) #в список класса добавь имя
    return dict(groups)          #превращаем его в обычный словарь


students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy"),
]

print(group_students(students))