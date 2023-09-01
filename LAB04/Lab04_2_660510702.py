#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab04_2
# 204111 Sec 002


def main():
    # รับค่า
    a = int(input())
    b = int(input())
    c = int(input())

    # เรียกใช้ฟังก์ชั่น
    my_min_mid_max(a, b,c)



def my_min_mid_max(a, b, c):
    
    # หา min โดยกำหนด min เป็น a ก่อน
    min_value = a
    if b < min_value:
        min_value = b
    if c < min_value:
        min_value = c

    # หา max โดยกำหนด min เป็น a ก่อน
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c

    # หา mid โดยเอาค่าทั้งหมดรวมกัน แล้ว ลบ min กับ max
    mid_value = a + b + c - min_value - max_value

    # แสดงค่า
    print ("min =",min_value)
    print ("mid =",mid_value)
    print ("max =",max_value)

if __name__ == '__main__':
    main()


    