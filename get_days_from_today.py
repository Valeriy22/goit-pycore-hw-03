from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    Параметри:
        date (str): рядок дати у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09')

    Повертає:
        int: кількість днів від заданої дати до поточної.
             Додатне число — дата в минулому, від'ємне — в майбутньому.

    Виключення:
        ValueError: якщо формат дати некоректний
    """
    try:
        # Перетворюємо рядок у об'єкт datetime
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        raise ValueError(
            f"Некоректний формат дати: '{date}'. Очікується формат 'РРРР-ММ-ДД'"
        )

    # Отримуємо поточну дату (без часу)
    today = datetime.today().date()

    # Розраховуємо різницю в днях
    difference = today - given_date

    return difference.days


# --- Приклади використання ---
if __name__ == "__main__":
    # Дата в минулому — додатний результат
    print(get_days_from_today("2022-02-22"))

    # Дата в майбутньому — від'ємний результат
    print(get_days_from_today("2027-01-01"))

    # Сьогоднішня дата — 0
    today_str = datetime.today().strftime("%Y-%m-%d")
    print(get_days_from_today(today_str))

    # Некоректний формат — ValueError
    try:
        print(get_days_from_today("09-10-2020"))
    except ValueError as e:
        print(f"Помилка: {e}")
