#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab09_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    test()

def left_max(list_a):

    # ถ้าลิสต์มีขนาด 1 หรือน้อยกว่า ให้คืนลิสต์เดิม
    if len(list_a) <= 1:
        return list_a
    
    # ถ้าตัวแรกมากกว่าตัวที่ 2 ให้ตัวที่สองเป็นตัวแรก
    if list_a[0] > list_a[1]:
        list_a[1] = list_a[0]
        return [list_a[0]] + left_max(list_a[1:])
    
    # เรียกฟังก์ชัน left_max ด้วยลิสต์ที่ยังไม่ถูกแทนที่
    return [list_a[0]] + left_max(list_a[1:])
    
def test():
    print(left_max([9, 8, 1, 9, 1]))
    print(left_max([3, 3, 1, 1, 2, 4]))
    
if __name__ == '__main__':
    main()