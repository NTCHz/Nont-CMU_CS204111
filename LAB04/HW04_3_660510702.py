#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW04_3
# 204111 Sec 002

def main():
    test_is_overlapped()

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):

    # คำนวณค่าของขอบเขตสี่เหลี่ยมทั้งสอง
    r1 = l1 + w1
    b1 = t1 + h1
    r2 = l2 + w2
    b2 = t2 + h2

    # ตรวจสอบว่าขอบเขตสี่เหลี่ยมทับกันหรือไม่
    if l1 <= r2 and r1 >= l2 and t1 <= b2 and b1 >= t2:
        return True # มีส่วนทับกัน
    else:
        return False # ไม่มีส่วนทับกัน

def test_is_overlapped():
    assert(is_overlapped(10, 10, 50, 75, 30, 55, 60, 60)) == True
    assert(is_overlapped(10, 10, 50, 75, 70, 55, 60, 60)) == False
    assert(is_overlapped(10, 10, 100, 150, 50, 100, 150, 200)) == True

if __name__ =="__main__":
    main()