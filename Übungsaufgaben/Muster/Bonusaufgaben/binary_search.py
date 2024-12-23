from typing import List


def binary_search_iterative(a: List[int], x: int) -> int:
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(a: List[int], x: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2

    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search_recursive(a, x, left, mid-1)
    else:
        return binary_search_recursive(a, x, mid+1, right)
