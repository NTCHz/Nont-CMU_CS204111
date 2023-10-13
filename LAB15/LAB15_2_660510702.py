#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB15_2
# 204111 Sec 002

def main():
    list_x = ([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]])
    # reshape(list_x)
    # print(list_x)
    # list_x = ([[2, 3, 4], [1, 2, 3],[1, 2, 3]])
    reshape(list_x)
    print(list_x)
    # list_x = ([[1, 2],[3, 4],[5, 6]])
    # reshape(list_x)
    # print(list_x)

def my_id():
    return "660510702"

def reshape(matrix):

    matrix_linear = []
    for i in matrix:
        matrix_linear.extend(i)

    len_matrix = len(matrix_linear)
    m = 2
    while True:
        n = m-1
        if m*n >= len_matrix:
            break
        n += 1
        if m*n >= len_matrix:
            break
        m += 1

    matrix[:] = [[0]*m for _ in range(n)]

    row = 0
    col = 0
    for i in matrix_linear:
        if col == m:
            row += 1
            col = 0
        matrix[row][col] = i
        col += 1

if __name__ == '__main__':
    main()