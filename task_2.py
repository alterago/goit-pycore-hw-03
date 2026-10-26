"""Task 2: a set of unique random numbers for a lottery ticket."""

import random

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 1000


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Return a sorted list of ``quantity`` unique random numbers from min to max.

    The parameters must satisfy 1 <= min <= max <= 1000 and the range must hold
    at least ``quantity`` numbers; otherwise the function returns an empty list.
    """
    params = (min, max, quantity)
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in params):
        return []
    if not LOWEST_NUMBER <= min <= max <= HIGHEST_NUMBER:
        return []
    if not 1 <= quantity <= max - min + 1:
        return []

    # random.sample picks without repetition, so every number is unique.
    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(0, 49, 6))   # min below 1 -> []
    print(get_numbers_ticket(1, 5, 10))   # not enough numbers -> []
