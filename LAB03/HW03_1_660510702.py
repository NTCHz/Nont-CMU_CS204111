#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW03_1
# 204111 Sec 002

import math

def main():
    test_nearest_odd()


# implement ฟังก์ชันนี้ให้ถูกต้อง
def  nearest_odd(x):

    #สูตรหาเลขคี่ที่ใกล้ที่สุด
    nearest_odd = 2 * math.ceil(x / 2) - 1
    return nearest_odd


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd():
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")


if __name__ == '__main__':
    main()