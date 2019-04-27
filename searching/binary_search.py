from typing import List


def binary_search(arr: List[int], key: int) -> int:
    """
        Assume that the list is sorted

        >>> arr = [3, 6, 7, 9, 12, 16]
        >>> binary_search(arr, 6)
        1
        >>> binary_search(arr, 9)
        3
        >>> binary_search(arr, 12)
        4
        >>> binary_search(arr, 0)
        -1
    """
    start = 0
    end = len(arr)  # end is always one greater than the final index

    while start < end:
        m = (start + end) // 2
        if arr[m] == key:
            return m
        elif arr[m] < key:
            start = m + 1
        else:
            end = m
    return - 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
