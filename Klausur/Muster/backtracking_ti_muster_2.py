# Aufgabe 2

from typing import List, Tuple
from copy import deepcopy


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


def backtracking(org_list: List[List[int]]) -> List[List[int]]:
    def complete(org_list: List[List[int]], config: List[List[int]], runs_: List[List[List[int]]]) -> Tuple[bool, List[List[int]]]:
        if is_complete(config):
            runs_.append(deepcopy(config))
            return False, config

        for new_list in org_list:
            config.append(new_list)
            if is_allowed(config):
                if complete(org_list, config, runs_)[0]:
                    return True, config
            config.pop()
        return False, []

    runs = []
    complete(org_list, [], runs)
    return min(runs, key=lambda x: len(x))


print(backtracking([[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 1]]))
