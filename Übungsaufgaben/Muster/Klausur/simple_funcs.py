from typing import List


def filter_even(a: List[int]) -> List[int]:
    return [digit for digit in a if (digit // 2) * 2 == digit]


def count_digits(n: int) -> int:
    counter = 0
    while n > 0:
        n //= 10
        counter += 1
    return counter


def count_digits_recursive(n: int) -> int:
    if n < 10:
        return 1
    return count_digits_recursive(n // 10) + 1


def count_long_words(a: List[str]) -> int:
    return len([word for word in a if len(word) > 5])


def count_fancy_long_words(a: List[str]) -> int:
    return len([word for word in a if len(word) > 5 and "e" in word.lower()])


def count_divisible_by_3_xor_5(nums: List[int]) -> int:
    return sum(1 for num in nums if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0))
