from typing import List


def matrix_multiply(mat1: List[List], mat2: List[List]):
    row1 = len(mat1)
    row2 = len(mat2)
    col1 = len(mat1[0])
    col2 = len(mat2[0])

    if col1 != row2:
        raise Exception("in dota zarb pazir nistan")

    result = [[0 for j in range(col2)] for i in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k] * mat2[k][j]


    return result


print(matrix_multiply([[5, 1], [3, 3]], [[4], [2]]))