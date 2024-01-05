https://github.com/souvikchand/oss101-forked/blob/souvikchand-details/gist-solutions.md
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Parameters:
    - arr (list): The sorted array to search.
    - target: The target element to find in the array.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
