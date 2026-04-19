"""
Поиск и удаление дубликатов
Напишите программу, которая удаляет дублирующиеся строки из файла
и сохраняет результат в новый файл.

- Имя нового файла формируется как unique_<original_filename>.
- Если файл не существует, программа должна вывести ошибку.
- Исходный порядок строк должен сохраниться.
- Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.
"""
import os
import sys

filename = "../python_dam_28_11_25/55_summary_14/movies_to_watch.txt"

try: # Пытаемся открыть файл
    with open(filename, "r", encoding="utf-8") as file:
        # "r" → режим чтения, encoding → корректная работа с текстом
        lines = file.readlines()
        # Читаеt ВСЕ строки файла в список

except FileNotFoundError:# ЕСЛИ ФАЙЛ НЕ НАЙДЕН
    print(f"Ошибка: файл '{filename}' не существует.")
    
    sys.exit(1) # Завершаем программу

new_filename = os.path.join(os.path.dirname(filename),
    # Берём папку, где лежит файл
    f"unique_{os.path.basename(filename)}"
    # Создаём новое имя файла
)

# УДАЛЕНИЕ ДУБЛИКАТОВ И ЗАПИСЬ

with open(new_filename, "w", encoding="utf-8") as file:
    # Открываем новый файл для записи
    # "w" → создаёт или перезаписывает файл

    file.writelines(list(dict.fromkeys(lines)))
    # dict.fromkeys(lines)
    # → создаёт словарь, где ключи — строки
    # → словарь НЕ хранит дубликаты
    # list(...)→ превращаем обратно в список
    # writelines(...)→ записываем строки в файл