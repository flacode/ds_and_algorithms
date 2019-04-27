from typing import List


def binary_search(arr: List[int], start: int, end: int, key: int) -> int:
    """
        Assume that the list is sorted

        >>> arr = [3, 6, 7, 9, 12, 16]
        >>> binary_search(arr, 0, len(arr), 6)
        1
        >>> binary_search(arr, 0, len(arr), 9)
        3
        >>> binary_search(arr, 0, len(arr), 12)
        4
        >>> binary_search(arr, 0, len(arr), 0)
        -1
    """

    while start >= end:
        return - 1  # not found

    m = (start + end) // 2
    if arr[m] == key:
        return m
    elif arr[m] < key:
        return binary_search(arr, m+1, end, key)
    else:
        return binary_search(arr, start, m, key)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
