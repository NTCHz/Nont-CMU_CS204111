#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW12_2
# 204111 Sec 002

import sys

def my_id():
    return "660510702"

def main():
    treasures = read_input()
    print(total_value('Gold', treasures))

    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1


def read_input():
    treasures = {}
    list_ = []

    # ลบบรรทัดที่มี "#" ออก
    for line in sys.stdin:
        if line.startswith("#"):
            continue
        a = line.replace("\n","")
        a = a.split(", ")
        list_.append([line])

    # สร้าง dict ที่มี treasure_type เป็น Keywords
    for i in list_:
        for j in i:
            a = j.replace("\n","")
        a = a.split(", ")
        treasures[a[1]] = []

    # เพิ่ม value เข้าไปใน dict
    for i in list_:
        for j in i:
            a = j.replace("\n","")
        a = a.split(", ")
        if a[0] != a[1]:
            treasures[a[1]] += [(a[0], int(a[2]))]

    # คืนค่า
    return treasures


def total_value(treasure_type, treasures):

    total = 0
    # ถ้า treasure_type อยู่ใน dict ให้ total += value แต่ถ้าไม่มีให้ total เป็น -1
    if treasure_type in treasures:
        a = treasures[treasure_type]
        for i in a:
            total += i[1]
    else:
        total = -1

    # คืนค่า
    return total


if __name__ == '__main__':
    main()
