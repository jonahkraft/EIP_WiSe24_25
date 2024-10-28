# Aufgabe 1

from typing import List, Tuple


def is_complete(config: List[List[int]]) -> bool:
    return all(1 in i for i in list(zip(*config))) and len(config) > 0


def count_1(config: List[List[int]]) -> int:
    return sum([1 if 1 in i else 0 for i in list(zip(*config))])


def is_allowed(config: List[List[int]]) -> bool:
    for item in config:
        if config.count(item) > 1:
            return False
    if count_1(config) == count_1(config[:-1]):
        return False
    return True


def complete(org_list: List[List[int]], config: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    if is_complete(config):
        return True, config

    for new_list in org_list:
        config.append(new_list)
        if is_allowed(config):
            if complete(org_list, config)[0]:
                return True, config
        config.pop()
    return False, []


print(complete([[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 1]], [])[1])
