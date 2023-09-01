#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW05_2
# 204111 Sec 002

import string

def main():
    test_rotate()


# implement this function
def rotate(num, pos):
    
    #แปลง int เป็น str
    num = str(num)

    # mod ด้วยจำนวนเพื่อหาตำแหน่ง
    pos %= len(num)

    #ส่งค่าคืน พร้อมเปลี่ยนเป็น int 
    return int(num[0-pos:] + num[:0-pos])

# test function
def test_rotate():

    assert(rotate(12345, 3)) == 34512
    assert(rotate(12345, 2)) == 45123
    assert(rotate(12345, -3)) == 45123
    assert(rotate(12345, -103)) == 45123


if __name__ == "__main__":
    main()
