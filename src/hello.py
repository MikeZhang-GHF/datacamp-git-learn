def binary_search(arr, x):
    """
    Searches for a value x in a sorted array using binary search.

    :param arr: List[int], a sorted array to search for the value x.
    :param x: int, the value to search for in the array.
    :return: The index of the value x in the array if it exists, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

