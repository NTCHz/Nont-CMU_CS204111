#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab11_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    print(matching_sum((1,), 1))
    print(matching_sum((5, 2), 7))
    print(matching_sum((10, -1, 1, -8, 3, 1), 2))
    print(matching_sum((10, -1, 1, -8, 3, 1), 10))
    

def matching_sum(t, target_value):
    # กำหนดตัวแปล
    a = set()
    d = {}

    # เพิ่ม keyword ลงใน dict
    for i in t:
        d[i] = 0

    # เพิ่มจำนวนข้อมูลใน keyword แต่ละตัว และเพิ่มสมาชิกลงไปใน set
    for i in t:
        d[i] += 1
        a.add(i) 

    for num in a:
        com = target_value - num
        # กรณีที่เอา target - จำนวนแล้วได้จำนวนนั้นให้เช็คอีกว่ามีกี่ตัวใน dict แล้วจึงคืนค่าตัวนั้น
        if  com == num and d[num] >= 2:
            return [num, target_value - num]
        
        # กรณีที่ target - จำนวน แล้วได้จำนวนที่อยู่ใน set a แต่ต้องไม่ได้ตัวเอง แล้วจึงคืนค่าตัวนั้น
        if com in a and com != num:
            return [num, target_value - num]
            
    # คืนค่ากรณีที่ไม่มีตัวไหนเลย
    return []


if __name__ == '__main__':
    main()