#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW13_1
# 204111 Sec 002

import copy

def main():
    print(square_matrix([[2, 3, 4], [1, 2, 3]]))
    print(square_matrix([[1, 2], [1, 2, 3],[1] ,[1, 2], [1, 2]]))
    print(square_matrix([[1, 2], [3, 4], [5, 6]] ))
    # pass

def my_id():
    return '660510702'

def square_matrix(list_x):

    row = len(list_x)
    col = 0

    for i in list_x:
        if len(i) > col:
            col = len(i)
    # เพิ่ม col
    if row >= col:
        for i in list_x:
            i.extend([0]*(row - len(i)))
    else:
        for i in list_x:
            i.extend([0]*(col - len(i)))

    # เพิ่ม row
    if row < col:
        for i in range (col-row):
            list_x.append([0] * col)

    return list_x
    

if __name__ == '__main__':
    main()