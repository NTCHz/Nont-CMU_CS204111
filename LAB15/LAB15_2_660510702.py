#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB15_2
# 204111 Sec 002

def main():
    # list_x = ([
    #     [1, 2], 
    #     [1, 2, 3], 
    #     [1, 2], 
    #     [1, 2], 
    #     [1]
    # ])
    # reshape(list_x)
    # print(list_x)
    # list_x = ([[2, 3, 4], [1, 2, 3]])
    list_x = ([[1, 2],[3, 4],[5, 6]])
    reshape(list_x)
    print(list_x)

def my_id():
    return "660510702"

def reshape(matrix):
    row_origin = len(matrix)
    col_origin = max(len(s) for s in matrix)
    if col_origin - row_origin == 1:
        print(1)
        return 
    else:
        print(col_origin)
        print(row_origin)
        r = min(row_origin, col_origin)
        result = []
        matrix_copy = []

        for i in matrix:
            matrix_copy.extend(i)
    
        total_len = len(matrix_copy)
        count = 0
        while True :
            if r * (r+1) > total_len:
                total_len = 0
                
                total_len = len(matrix_copy)

                if total_len < r * (r+1):
                    matrix_copy.extend([0])
                    continue
                
                for k in range(r):
                    cur = []
                    for _ in range(r+1):
                        cur += [matrix_copy[count]]
                        count += 1

                    result.append(cur)
                break
            r += 1

        matrix[:] = result

if __name__ == '__main__':
    main()