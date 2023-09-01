#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab03_1
# 204111 Sec 002

import math


def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(radius)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print("volume = {0:.2f}".format(volume))

    # ฟังก์ชั่นหา r โดยมาจากสมการพื้นที่ผิวรอบทรงกลม 4(pi)r**2
def find_r_from_surface_area(surface_area):
    r = math.sqrt(surface_area/(4*math.pi))
    return r

    # ฟังก์ชั่นหา พื้นที่รูปทรงกลมโดยมาจากสมการ 4/3(pi)r**3
def sphere_volume(radius):
    x = 4/3*math.pi*(radius**3)
    return x


if __name__ == '__main__':
    main()
