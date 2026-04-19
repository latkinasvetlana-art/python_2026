"""
Фильтрация по ключевому слову
Напишите программу, которая ищет в файле все строки,
содержащие указанное пользователем слово, и сохраняет их в новый файл.

- Имя нового файла формируется как <keyword>_<original_filename>.
- Если файл не существует, программа должна вывести ошибку.
- Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.
"""
import os # Модуль для работы с путями 
import sys # Модуль для работы с системой 

filename = "../python_dam_28_11_25/55_summary_14/system_log.txt" # Путь к файлу, который мы будем читать
keyword = input("Введите ключевое слово: ").lower()

try: # Пытаемся открыть файл
    with open(filename, "r", encoding="utf-8") as file:
        # "r" → режим чтения
        # encoding → корректная работа с текстом
        # Читаем файл построчно
        # Оставляем только те строки, где есть keyword
        lines = [line for line in file if keyword in line.lower()]
        # line.lower() → чтобы сравнение было без учёта регистра
        print(lines)
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не существует.")

    sys.exit(1)
    # Завершаем программу (1 = ошибка)

if lines: # Проверяем: список НЕ пустой

    new_filename = os.path.join(os.path.dirname(filename),
        # Берём папку, где лежит файл
        f"{keyword}_{os.path.basename(filename)}"
        # Создаём новое имя файла, пример: "error_system_log.txt"
    )

    # Открываем новый файл для записи
    with open(new_filename, "w", encoding="utf-8") as file:
        # "w" → режим записи (создаёт или перезаписывает файл)

        file.writelines(lines)
        # Записываем все найденные строки
else:  # ЕСЛИ СОВПАДЕНИЙ НЕТ
    print("Совпадения не найдены.")
