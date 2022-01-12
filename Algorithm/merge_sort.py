from typing import List


def merge_sort(arr : List) -> List:
    arr_len = len(arr)

    if arr_len > 1:
        arr_len = arr_len // 2
        left = merge_sort(arr[:arr_len])
        right = merge_sort(arr[arr_len:])
        print("left: ", left)
        print("right: ", right)

        arr = []

        while left and right:
            if left[0] < right[0]:
                temp = left.pop(0)
                arr.append(temp)
            else:
                temp = right.pop(0)
                arr.append(temp)
        
        for elm in left:
            arr.append(elm)
        
        for elm in right:
            arr.append(elm)
        print(arr)
        return arr
        
    else:
        return arr
        
        


my_arr = [8,7,6,3,98]

print(merge_sort(my_arr))

    