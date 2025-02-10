from typing import Set, List


def is_complete(cover: List[Set[int]], universe: Set[int]) -> bool:
    # wir überprüfen, ob das Universum eine Teilmenge der Vereinigungsmenge der Überdeckungsmengen ist.
    # Wenn ja, dann ist die Überdeckung vollständig.
    return universe.issubset(set().union(*cover))


def set_cover(universe: Set[int], subsets: List[Set[int]], k: int, cover: List[Set[int]]) -> bool:

    if is_complete(cover, universe):
        return True

    if len(cover) >= k:
        # das Cover darf nicht mehr als k Teilmengen enthalten
        return False

    for subset in subsets:
        if subset not in cover:  # allowed-Abfrage
            cover.append(subset)  # Erweiterung
            if set_cover(universe, subsets, k, cover):
                return True
            cover.pop()  # Backtracking

    return False
