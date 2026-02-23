import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує набір унікальних випадкових чисел для лотерейного білета.

    Параметри:
        min (int): мінімальне можливе число (не менше 1)
        max (int): максимальне можливе число (не більше 1000)
        quantity (int): кількість чисел для вибору

    Повертає:
        list: відсортований список унікальних випадкових чисел,
              або пустий список, якщо параметри некоректні.
    """
    # Валідація вхідних параметрів
    if min < 1 or max > 1000:
        return []
    if min > max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []

    # random.sample гарантує унікальність чисел
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


# --- Приклади використання ---
if __name__ == "__main__":
    # Лотерея "6 із 49"
    print(get_numbers_ticket(1, 49, 6))       # напр. [4, 12, 23, 31, 42, 47]

    # Лотерея "5 із 36"
    print(get_numbers_ticket(1, 36, 5))       # напр. [3, 11, 17, 28, 35]

    # Лотерея "7 із 100"
    print(get_numbers_ticket(1, 100, 7))      # напр. [8, 22, 34, 56, 71, 88, 95]

    # Некоректні параметри — пустий список
    print(get_numbers_ticket(0, 49, 6))       # [] (min < 1)
    print(get_numbers_ticket(1, 1001, 5))     # [] (max > 1000)
    print(get_numbers_ticket(1, 5, 10))       # [] (quantity > діапазон)
    print(get_numbers_ticket(10, 5, 3))       # [] (min > max)
