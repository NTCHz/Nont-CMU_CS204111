#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW03_2
# 204111 Sec 002

def main():
    # รับข้อมูลจาก user
    number = float(input())
    k = float(input())

    # นำเลขที่ให้มาส่งไปยัง function
    digit = kth_digit(number, k)

    # แสดงเลขที่ต้องการตามหลัก
    print(int(digit))


def kth_digit(number, k):

    # สูตรหาเลขที่ต้องการตามหลัก
    kth_d = abs(number) % (10**(k+1)) // 10**k

    # ส่งค่าคืน
    return kth_d

if __name__ == '__main__':
    main()