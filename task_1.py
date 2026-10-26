"""Task 1: number of days between a given date and today."""

from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def get_days_from_today(date: str) -> int | None:
    """Return the number of days from ``date`` to today.

    ``date`` is a string in the 'YYYY-MM-DD' format. Only calendar days count:
    the time of day is ignored. A date later than today gives a negative number.
    An invalid date prints an error message and returns None.
    """
    try:
        given_date = datetime.strptime(date, DATE_FORMAT).date()
    except (TypeError, ValueError):
        print(f"Invalid date {date!r}: expected the 'YYYY-MM-DD' format.")
        return None

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2099-01-01"))
    print(get_days_from_today("09.10.2021"))
