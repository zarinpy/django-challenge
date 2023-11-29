from random import choices

__all__ = ["generate_random_numbers"]


def generate_random_numbers(n: int = 5) -> str:
    digits = choices(range(10), k=n)
    # Ensure the first digit is not 0 to maintain the specified number of digits
    if digits[0] == 0:
        digits[0] = choices(range(1, 10), k=1)[0]
    return ''.join(map(str, digits))
