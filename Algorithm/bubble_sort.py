from typing import List


def bubble_sort(arr: List) -> List:
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr



my_arr = [2, 9, 6, -1, 12, 176, 24, 1]

print(bubble_sort(my_arr))