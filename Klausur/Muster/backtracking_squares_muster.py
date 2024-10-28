from typing import List

# Aufgabe 1:
# Das ist in der Tat ein sehr naiver Ansatz. Sollte man lieber lassen.
# Die Liste A hat 25 Elemente und somit gibt es 25! (also etwa 1.551121e+25) Permutationen von A. Das sind sehr viele :)


def is_complete(config: List[int], n: int) -> bool:
    return len(config) == n


def is_allowed(config: List[int]) -> bool:
    if len(config) == 1:
        return True

    x: int = config[-1] + config[-2]
    return int(x**0.5) == x**0.5


def complete(config: List[int], digits: List[int], n: int) -> bool:
    if is_complete(config, n):
        return True

    for i in list(digits):
        config.append(i)
        digits.remove(i)
        if is_allowed(config):
            if complete(config, digits, n):
                return True
        config.remove(i)
        digits.append(i)
    return False



digits = [i for i in range(7, 32)]
configuration = []
complete(configuration, digits, len(digits))
config2 = configuration[::-1]
print(configuration)
print(config2)
