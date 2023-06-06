import sys

data = [1, 'hello', 3.14, True, [1, 2, 3], (4, 5, 6)]

# Добавление повторяющихся элементов
data.extend([1, 'hello', 3.14])

# Итерация по элементам списка
for index, value in enumerate(data, start=1):
    print(f"Порядковый номер: {index}")
    print(f"Значение: {value}")
    print(f"Адрес в памяти: {id(value)}")
    print(f"Размер в памяти: {sys.getsizeof(value)} байт")

    # Проверка на возможность хэширования объекта
    try:
        hash_value = hash(value)
        print(f"Хэш объекта: {hash_value}")
    except TypeError:
        print("Хэш объекта: Невозможно вычислить (нехэшируемый тип)")

    # Проверка на целое число, если значение положительное
    if isinstance(value, int) and value > 0:
        print("Результат проверки на целое число: True")

    # Проверка на строку, если значение положительное
    if isinstance(value, str) and len(value) > 0:
        print("Результат проверки на строку: True")

    print("------------------------")

