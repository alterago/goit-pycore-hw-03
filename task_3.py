"""Task 3: normalize phone numbers for an SMS mailing."""

import re

COUNTRY_CODE = "+38"


def normalize_phone(phone_number: str) -> str:
    """Return the phone number as '+' and digits, with the Ukrainian code added.

    Every character except digits and a leading '+' is removed. A number that
    starts with '380' gets '+'; a number without a country code gets '+38'.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())
    # Keep '+' only as the first character.
    cleaned = cleaned[:1] + cleaned[1:].replace("+", "")

    if cleaned.startswith("+"):
        return cleaned
    if cleaned.startswith("380"):
        return "+" + cleaned
    return COUNTRY_CODE + cleaned


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized phone numbers for the SMS mailing:", sanitized_numbers)
