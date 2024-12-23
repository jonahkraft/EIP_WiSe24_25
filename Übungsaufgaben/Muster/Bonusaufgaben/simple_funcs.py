from typing import List, Any

def create_boolean_grid(n: int) -> List[List[bool]]:
    return [[i+j % 3 == 0 for j in range(n)] for i in range(n)]


def left_shift(a: list) -> None:
    for i in range(len(a) - 1):
        a[i], a[i+1] = a[i+1], a[i]


def deepcopy(a: List[Any]) -> List[Any]:
    r = []
    for i in a:
        if not isinstance(i, list):
            r.append(i)
        else:
            r.append(deepcopy(i))
    return r


def ggt(a: int, b: int) -> int:
    if b == 0:
        return a
    return ggt(b, a % b)


def avg(a: List[int], s: int = 0, i: int = 0) -> float:
    if 0 == len(a):
        return 0
    elif i == len(a):
        return s / i
    else:
        return avg(a, s+a[i], i+1)


def len_recursive(a: List[Any], i: int = 0) -> int:
    if a == []:
        return i
    else:
        return len_recursive(a[1:], i + 1)


def count_even(a: List[int], i: int = 0) -> int:
    if i == len(a):
        return 0
    elif a[i] % 2 == 0:
        return 1 + count_even(a, i+1)
    else:
        return count_even(a, i+1)


def is_prime(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime(a: List[int], i: int = 0) -> int:
    if i == len(a):
        return 0
    elif is_prime(a[i]):
        return 1 + count_prime(a, i+1)
    else:
        return count_prime(a, i+1)
