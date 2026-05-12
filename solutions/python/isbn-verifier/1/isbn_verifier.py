import re


def is_valid(isbn: str) -> bool:
    """
    Validate whether a string is a valid ISBN-10.

    The function accepts ISBN-10 values with or without hyphens.
    The last character may be a digit or 'X', where 'X' represents 10.

    Args:
        isbn: ISBN-10 string to validate.

    Returns:
        True if the ISBN-10 is valid, otherwise False.
    """

    # Reject invalid characters
    if re.search(r"[^0-9Xx-]", isbn):
        return False

    # Extract digits and X
    values = re.findall(r"[\dX]", isbn, flags=re.IGNORECASE)

    # ISBN-10 must contain exactly 10 characters
    if len(values) != 10:
        return False

    # X is only allowed as the check digit
    if any(value.upper() == "X" for value in values[:-1]):
        return False

    total = 0

    for i, value in enumerate(values):
        number = 10 if value.upper() == "X" else int(value)
        total += number * (10 - i)

    return total % 11 == 0