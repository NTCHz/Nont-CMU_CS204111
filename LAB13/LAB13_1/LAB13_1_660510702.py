#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB13_1
# 204111 Sec 002

def main():
    print(matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
    print(matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8, 5, 9, 3], [9, 10, -3, 7, 13], [11, 12, 6, 2, 9]] ))

def my_id():
    return '660510702'

def matrix_mult(m1, m2):

    # ตรวจสอบว่าเมทริกซ์ m1 และ m2 สามารถทำการคูณกันได้หรือไม่
    if len(m1[0]) != len(m2):
        return None

    # กำหนดขนาดของเมทริกซ์
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    # คำนวณผลคูณและเก็บในเมทริกซ์ผลลัพธ์
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    # คืนค่า
    return result


if __name__ == '__main__':
    main()