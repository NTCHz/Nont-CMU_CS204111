#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab04_1
# 204111 Sec 002


# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()
from math import isclose

def main():
    test_circle_intersect()


def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6):

    # สูตรหาระยะห่างระหว่างจุด
    distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

    # กรณีที่ระยะห่างมากกว่า รัศมีทั้งสอง
    if distance - (r1+r2) > epsilon :
        return -1
    
    # กรณีที่เท่ากัน
    elif isclose(r1+r2, distance, abs_tol=epsilon):
        return 0
    
    # กรณีที่น้อยกว่า
    else:
        return 1

def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()
