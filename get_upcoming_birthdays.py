from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Визначає, кого з колег потрібно привітати з днем народження
    протягом наступних 7 днів (включаючи сьогодні).

    Якщо день народження припадає на вихідний — дата привітання
    переноситься на наступний понеділок.

    Параметри:
        users (list): список словників з ключами 'name' та 'birthday'
                      (формат дати: 'РРРР.ММ.ДД')

    Повертає:
        list: список словників з ключами 'name' та 'congratulation_date'
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Перетворюємо рядок дати народження в об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Переносимо день народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження в межах 7 днів
        days_until = (birthday_this_year - today).days
        if days_until > 7:
            continue

        # Якщо припадає на вихідний — переносимо на понеділок
        congratulation_date = birthday_this_year
        if congratulation_date.weekday() == 5:      # субота
            congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:    # неділя
            congratulation_date += timedelta(days=1)

        upcoming.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return upcoming


# --- Приклади використання ---
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

    # Тест з поточними датами (відносно сьогодні)
    today = datetime.today().date()
    test_users = [
        {"name": "Олег", "birthday": (today).strftime("1990.%m.%d")},
        {"name": "Анна", "birthday": (today + timedelta(days=3)).strftime("1992.%m.%d")},
        {"name": "Марія", "birthday": (today + timedelta(days=7)).strftime("1988.%m.%d")},
        {"name": "Іван", "birthday": (today + timedelta(days=10)).strftime("1995.%m.%d")},
    ]

    print("\nТест з динамічними датами:")
    for entry in get_upcoming_birthdays(test_users):
        print(f"  {entry['name']} — привітати {entry['congratulation_date']}")
