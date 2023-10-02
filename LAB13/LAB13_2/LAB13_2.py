#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB13_2
# 204111 Sec 002

def main():
    print (read_pixel([
    [1, 2, 6], 
    [3, 5, 7], 
    [4, 8, 9]
    ]))
    print (read_pixel([
    [7, 12, 1], 
    [2, 13, 8], 
    [16, 3, 10]
    ]))
    print (read_pixel([
    [20, 15, 12, 0, 0, 0, 0, 0],
    [15, 17, 0, 0, 0, 0, 0, 0,],
    [12, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]))

def my_id():
    return '660510702'

def read_pixel(pixel_block):

    # ตัวแปรเก็บคำตอบ
    result = []

    # จำนวนรอบ
    lenght = len(pixel_block) + len(pixel_block[0]) - 1

    for i in range(lenght):
        for j in range(len(pixel_block)):
            for k in range(len(pixel_block)):
                if k+j == i and k > i:
                    result.append(pixel_block[k][j])
                
                if k+j == i and k <= i and i % 2 == 1:
                    result.append(pixel_block[j][k])

                if k+j == i and k <= i and i % 2 == 0:
                    result.append(pixel_block[k][j])
        
    # คืนค่า
    return result

if __name__ == '__main__':
    main()
