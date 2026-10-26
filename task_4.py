"""Task 4: colleagues to congratulate on their birthday in the coming week."""

from datetime import date, datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"
DAYS_AHEAD = 7  # today and the next six days
SATURDAY = 5
SUNDAY = 6


def birthday_in_year(birthday: date, year: int) -> date:
    """Return the birthday in ``year``; 29 February becomes 28 February in a common year."""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, day=28)


def move_from_weekend(day: date) -> date:
    """Return the following Monday for a Saturday or a Sunday, otherwise the day itself."""
    if day.weekday() == SATURDAY:
        return day + timedelta(days=2)
    if day.weekday() == SUNDAY:
        return day + timedelta(days=1)
    return day


def get_upcoming_birthdays(users: list[dict], today: date | None = None) -> list[dict]:
    """Return who to congratulate within 7 days, today included.

    Each user is a dict with 'name' and 'birthday' ('YYYY.MM.DD'). The result is
    a list of dicts with 'name' and 'congratulation_date' ('YYYY.MM.DD'); a
    birthday on a weekend is congratulated on the following Monday.
    ``today`` defaults to the current date and exists for testing.
    """
    today = today or datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        birthday_this_year = birthday_in_year(birthday, today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_in_year(birthday, today.year + 1)

        if (birthday_this_year - today).days < DAYS_AHEAD:
            congratulation_date = move_from_weekend(birthday_this_year)
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
            })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users, today=date(2024, 1, 22))
    print("Congratulations list for this week:", upcoming_birthdays)
