from typing import List


my_arr = [2, 3, 6, 8, 12, 25, 81]

#### iterative binary search
def iterative_binary_search(arr: List, elm) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if elm == arr[mid]:
            return mid
        
        elif elm < arr[mid]:
            high = mid - 1
        
        elif elm > arr[mid]:
            low = mid + 1

    return -1


# print(iterative_binary_search(my_arr, 12))

#### recursive binary search
def _recursive_binary_search(arr: List, low, high, elm):
    mid = (low + high) // 2

    if low <= high:
        if elm == arr[mid]:
            return mid
        elif elm < arr[mid]:
            return _recursive_binary_search(arr, low , mid -1, elm)
        else:
            return _recursive_binary_search(arr, mid +1  , high, elm)

    return -1

def recursive_binary_search(arr: List, elm):
    return _recursive_binary_search(arr, 0, len(my_arr) - 1, elm)


print(recursive_binary_search(my_arr, 45))


