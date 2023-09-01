#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab03_2
# 204111 Sec 002

import math


def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    x = float(input("x: "))


    # สร้างตัวแปร ส่งค่าเข้าไปในฟังค์ชั่น
    octagon_a = octagon_area(x)

    # แสดงผล
    print("octagon area = {0:.2f}".format(octagon_a))

    # ฟังก์ชั่นหาพื้นที่แปดเหลี่ยม
def octagon_area(x):

    # สูตรการคำนวนแปดเหลี่ยม
    octagon_a = (7/9) * x**2

    #ส่งค่าคืน
    return octagon_a


if __name__ == '__main__':
    main()
