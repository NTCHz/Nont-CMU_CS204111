#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW13_3
# 204111 Sec 002

def main():
    print (sum_d_product([[3, 3, 3, 2], 
 [2, 0, 3, 1], 
 [2, 1, 2, 3], 
 [1, 0, 2, -1]]))
    print (sum_d_product([[1, 1, 5, -1], 
 [12, 2, -2, 0], 
 [4, 8, 8, 12], 
 [4, 12, 12, 15]]))
    print (sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3], 
 [3, -1, -1, 2, 0, -1, 2, 1], 
 [3, 0, 1, 2, 3, 1, 3, 1], 
 [2, 2, 1, -1, -1, 2, 0, 3], 
 [1, 3, 2, 1, 3, 2, 2, 1], 
 [1, 2, 2, 1, 3, 3, 1, 3], 
 [2, 2, 2, 2, 2, 2, 3, 3], 
 [1, 3, 2, 3, 1, 1, 2, 2]]))

def my_id():
    return '660510702'

def sum_d_product(m):
    n = len(m)
    result = []
    cur = []

    if n == 2:
        return (m[0][0] * m[1][1] + m[0][1] * m[1][0])

    for i in range (0, n, 2):
        for j in range(0, n, 2):
            list_a = [[m[i][j],m[i][j+1]],[m[i+1][j],m[i+1][j+1]]]
            cur.append(list_a[0][0] * list_a[1][1] + list_a[0][1] * list_a[1][0])
        result.append(cur)
        cur = []

    return sum_d_product(result)

if __name__ == '__main__':
    main()