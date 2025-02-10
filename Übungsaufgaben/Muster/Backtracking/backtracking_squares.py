from typing import List

# Aufgabe 1:
# Die Liste A hat 25 Elemente und somit gibt es 25! (also etwa 1.551121e+25) Permutationen von A. Das sind sehr viele :)


def is_allowed(config: List[int]) -> bool:
    if len(config) < 2:
        return True  # Eine einzelne Zahl ist immer erlaubt

    # Summe muss eine Quadratzahl sein
    # mit % 1 kann man prüfen, ob eine Zahl eine ganze Zahl ist
    return (config[-1] + config[-2]) ** 0.5 % 1 == 0


def is_complete(config: List[int], n: int) -> bool:
    # es genügt, die Länge der Konfiguration zu prüfen
    return len(config) == n


def complete(config: List[int], digits: List[int], n: int) -> bool:
    if is_complete(config, n):
        return True

    for i in digits[:]:  # Kopie der Liste, um Änderungen während der Iteration zu vermeiden
        config.append(i)
        digits.remove(i)

        if is_allowed(config) and complete(config, digits, n):
            return True

        # Backtracking
        config.pop()
        digits.append(i)

    return False


if __name__ == "__main__":
    digits = list(range(7, 32))
    configuration = []

    if complete(configuration, digits, len(digits)):
        print("Lösung gefunden:", configuration)
        print("Umgekehrte Lösung:", configuration[::-1])
    else:
        print("Keine gültige Konfiguration gefunden.")
