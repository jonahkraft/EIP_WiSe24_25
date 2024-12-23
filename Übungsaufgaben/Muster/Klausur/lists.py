from typing import List


def reverse_array(array: List[int]) -> List[int]:
    for i in range(len(array)//2):
        array[i], array[-(i+1)] = array[-(i+1)], array[i]
    return array


def reverse_array_recursively(array: List[int], start: int = 0, end: int = -1) -> List[int]:
    if end == -1:
        end = len(array)-1
    if start >= end:
        return array
    array[start], array[end] = array[end], array[start]
    return reverse_array_recursively(array, start+1, end-1)
