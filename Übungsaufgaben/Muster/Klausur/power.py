# die Funktionen berechnen a^b


def pow_iterative(a: int, b: int) -> int:
    p: int = a
    for _ in range(b-1):
        p *= a
    return p


def pow_recursively(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * pow_recursively(a, b-1)
